# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import ujson

class Crawler():

    def __init__(self, url, rooms_limit=5):
        self.rooms_limit = rooms_limit
        self.url = url

    def crawl(self):
        data = self._make_request(self.url)
        raw_rooms = self._get_rooms(data)
        rooms = []
        for raw_room in raw_rooms:
            if len(rooms) >= self.rooms_limit:
                break;
            rooms.append(self._parse_room(raw_room))
        return rooms

    def _make_request(self, url):
        result = requests.get(url).text
        return result

    def _get_rooms(self, data):
        raise NotImplementedError()

    def _parse_room(self, room):
        raise NotImplementedError()


class DouyuCrawler(Crawler):

    root_url = 'http://www.douyutv.com'

    def _get_rooms(self, data):
        data = BeautifulSoup(data, "html.parser")
        return data.find(id='item_data').find_all('li')

    def _parse_room(self, room):
        room_data = {}
        room_data['image_url'] = self._get_image_url(room)
        room_data['url'] = self._get_url(room)
        room_data['name'] = self._get_name(room)
        room_data['total_viewers'] = self._get_total_viewers(room)
        room_data['streamer'] = self._get_streamer(room)
        return room_data

    def _get_image_url(self, room):
        return room.img['data-original']

    def _get_url(self, room):
        return self.root_url + room.a['href']

    def _get_name(self, room):
        return room.h1.string

    def _get_total_viewers(self, room):
        return room.select('span.view')[0].string

    def _get_streamer(self, room):
        return room.select('span.nnt')[0].string


class TwitchCrawler(Crawler):

    def _get_rooms(self, data):
        data = ujson.loads(data)
        return data['streams']

    def _parse_room(self, room):
        room_data = {}
        room_data['image_url'] = self._get_image_url(room)
        room_data['url'] = self._get_url(room)
        room_data['name'] = self._get_name(room)
        room_data['total_viewers'] = self._get_total_viewers(room)
        room_data['streamer'] = self._get_streamer(room)
        return room_data

    def _get_image_url(self, room):
        return room['preview']['medium']

    def _get_url(self, room):
        return room['channel']['url']

    def _get_name(self, room):
        return room['channel']['status']

    def _get_total_viewers(self, room):
        return room['viewers']

    def _get_streamer(self, room):
        return room['channel']['display_name']
