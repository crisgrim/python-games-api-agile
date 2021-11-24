from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class BelongsTo(models.Model):
    """
    BelongsTo:
        This class extends from the **base model** provided by Django.
        Include the **added_by** field in all the views that inherit from it.
        The **added_by** field represents the relationship with the user who creates the element.
    """
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CreatedDate(models.Model):
    """
    CreatedDate:
        This class extends from the **base model** provided by Django.
        Include the **created_date** field in all the views that inherit from it.
        The **created_date** is the field to keep a timestamp when the element was created.
    """
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


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


class Game(BelongsTo, CreatedDate):
    """
    Game:
        This model inherits the properties from the classes: BelongsTo and CreatedDate.
        And the **base model** provided by Django because these classes inherit from it.
        Added the field **name** with a maximum length of 200 letters.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Party(BelongsTo, CreatedDate):
    """
    Party:
        This model inherits the properties from the classes: BelongsTo and CreatedDate.
        And the **base model** provided by Django because these classes inherit from it.
        Added the field **name** with a maximum length of 200 letters.
        The **game_id** field represents the relationship to the game to which this party belongs.
    """
    name = models.CharField(max_length=200)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(BelongsTo, CreatedDate):
    """
    Message:
        This model inherits the properties from the classes: BelongsTo and CreatedDate.
        And the **base model** provided by Django because these classes inherit from it.
        Added the field **content** with a maximum length of 200 letters.
        The **party_id** field represents the relationship to the party to which this message belongs.
    """
    content = models.CharField(max_length=200)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
