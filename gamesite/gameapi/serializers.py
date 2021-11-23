from rest_framework import serializers
from .models import Game, Party, Message, CustomUser


class UserSerializer(serializers.ModelSerializer):
    """
    UserSerializer:
        This serializer takes CustomUser as a base model.
        Returns from the user only the relevant information:
            - username
            - email
            - steam_user
            - discord_user
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'steam_user', 'discord_user']


class GameSerializer(serializers.HyperlinkedModelSerializer):
    """
    GameSerializer:
        This serializer takes Game as a base model.
        Returns from the game all the information:
            - name
            - added_by
            - created_date
    """
    added_by = UserSerializer()

    class Meta:
        model = Game
        fields = ('name', 'added_by', 'created_date')


class PartySerializer(serializers.HyperlinkedModelSerializer):
    """
    PartySerializer:
        This serializer takes Party as a base model.
        Returns from the party all the information:
            - name
            - added_by
            - created_date
            - game_id
    """
    added_by = UserSerializer()

    class Meta:
        model = Party
        fields = ('name', 'added_by', 'created_date', 'game_id')


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    """
    MessageSerializer:
        This serializer takes Message as a base model.
        Returns from the message all the information:
            - content
            - added_by
            - created_date
            - party_id
    """
    added_by = UserSerializer()

    class Meta:
        model = Message
        fields = ('content', 'added_by', 'created_date', 'party_id')
