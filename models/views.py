from django.shortcuts import render
from .models import Game


def index(request):
    game = Game.objects.get(name='hearthstone')

    context = {}
    context['rooms_by_platform_name'] = _get_rooms_by_platform_name(game)
    context['game_name'] = game.name
    context['games'] = Game.objects.all()
    return render(request, 'models/index.html', context)


def _get_rooms_by_platform_name(game):
    rooms = {}
    for platform_game in game.platformgame_set.all():
        rooms[platform_game.platform_name] = platform_game.room_set.all()
    return rooms


def rooms(request, game_id):
    game = Game.objects.get(pk=game_id)

    context = {}
    context['rooms_by_platform_name'] = _get_rooms_by_platform_name(game)
    context['game_name'] = game.name
    context['games'] = Game.objects.all()
    return render(request, 'models/index.html', context)

