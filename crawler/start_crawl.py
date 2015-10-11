import sys
sys.path.append('./')
from lib.config import create_app
create_app('local')
import django
django.setup()

import time

import gevent

import crawler
from models import PlatformGame, Room


crawlers_by_platform_name = {
    'douyu': crawler.DouyuCrawler,
    'twitch': crawler.TwitchCrawler,
}


def worker(crawler, platform_game):
        """thread worker function"""
        rooms = crawler.crawl()
        print '***********\n' + platform_game.platform_name + '\n***********'
        for room in rooms:
            print room
        start = time.time()
        _store_rooms(rooms, platform_game)
        print 'Time cost: ', time.time() - start
        

def _store_rooms(rooms, platform_game):
    existing_rooms = platform_game.room_set.all()
    new_rooms = iter(rooms)
    for room in existing_rooms:
        try:
            new_room = new_rooms.next()
        except StopIteration:
            room.delete()
            continue
        room.name = new_room['name']
        room.url = new_room['url']
        room.image_url = new_room['image_url']
        room.total_viewers = new_room['total_viewers']
        room.streamer = new_room['streamer']
        room.save()
    for new_room in new_rooms:
        Room(
            platform_game=platform_game,
            name=new_room['name'],
            url=new_room['url'],
            image_url=new_room['image_url'],
            total_viewers=new_room['total_viewers'],
            streamer=new_room['streamer'],
        ).save()


def run():
    jobs = []
    platform_games = PlatformGame.objects.all()
    while(True):
        for platform_game in platform_games:
            crawler = _create_crawler_from_platform_game(platform_game)
            jobs.append(gevent.spawn(worker, crawler, platform_game))
        gevent.joinall(jobs, timeout=5)
        break


def _create_crawler_from_platform_game(platform_game):
    crawler_class = crawlers_by_platform_name[platform_game.platform_name]
    return crawler_class(url=platform_game.url)


if __name__ == "__main__":
    run()
