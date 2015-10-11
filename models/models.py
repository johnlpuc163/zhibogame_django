from django.db import models


class Platform(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class PlatformGame(models.Model):

    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    game  = models.ForeignKey(Game, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    url = models.CharField(max_length=500)

    game_name = models.CharField(max_length=200)

    platform_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Room(models.Model):

    platform_game = models.ForeignKey(PlatformGame, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    url = models.CharField(max_length=500)

    image_url = models.CharField(max_length=500)

    total_viewers = models.CharField(max_length=200)

    streamer = models.CharField(max_length=200)

    index = models.IntegerField(default=0)

    def __unicode__(self):
        return self.streamer
