from django.contrib import admin

from .models import (
    Game,
    Platform,
    PlatformGame,
    Room,
)


class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PlatformAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class PlatformGameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'platform', 'game']


class RoomGameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'streamer', 'platform_game']


admin.site.register(Game, GameAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(PlatformGame, PlatformGameAdmin)
admin.site.register(Room, RoomGameAdmin)