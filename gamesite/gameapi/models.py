from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    CustomUser:
        This model extends from the **AbstractUser** provided by Django.
        Changed the **email** to be a unique field to prevent having two users with the same email.
        Added two custom fields (steam_user and discord_user) that are optional with a maximum length of 100 letters.
    """
    email = models.EmailField('email address', unique=True)
    steam_user = models.CharField(blank=True, max_length=100)
    discord_user = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.email


class Game(models.Model):
    """
    Game:
        This model extends from the model base provided by Django.
        Added the field name with a maximum length of 200 letters.
        The added by field represent the relationship with the user who creates the game.
        The created date is the field to keep a timestamp when the game was created.
    """
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Party(models.Model):
    """
    Party:
        This model extends from the model base provided by Django.
        Added the field name with a maximum length of 200 letters.
        The added by field represents the relationship with the user who creates the party.
        The created date is the field to keep a timestamp when the party was created.
        The game id field represents the relationship to the game which this party belongs.
    """
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    """
    Message:
        This model extends from the model base provided by Django.
        Added the field content with a maximum length of 200 letters.
        The added by field represents the relationship with the user who creates the message.
        The created date is the field to keep a timestamp when the message was created.
        The party id field represents the relationship to the party which this message belongs.
    """
    content = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
