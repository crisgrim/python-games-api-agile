from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GameSerializer, PartySerializer, MessageSerializer, UserSerializer
from .models import Game, Party, Message, CustomUser


class Filterable:
    """
    Filterable:
        Include the fields related to applying filters in all the views that inherit from it.
    """
    filter_backends = [DjangoFilterBackend]
    filterset_fields = []


class GameViewSet(viewsets.ModelViewSet, Filterable):
    """
    GameViewSet:
        Returns a list of all **games** in the system, ordered by name.
        Uses the **GameSerializer** as serializer class.
        Provide the way to filter the games by **name**.
    """
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    filterset_fields = ['name']


class PartyViewSet(viewsets.ModelViewSet, Filterable):
    """
    PartyViewSet:
        Returns a list of all **parties** in the system, ordered by name.
        Uses the **PartySerializer** as serializer class.
        Provide the way to filter the games by **game_id**.
    """
    queryset = Party.objects.all().order_by('name')
    serializer_class = PartySerializer
    filterset_fields = ['game_id']


class MessageViewSet(viewsets.ModelViewSet, Filterable):
    """
    MessageViewSet:
        Returns a list of all **messages** in the system, ordered by created_date.
        Uses the **MessageSerializer** as serializer class.
        Provide the way to filter the games by **party_id**.
    """
    queryset = Message.objects.all().order_by('created_date')
    serializer_class = MessageSerializer
    filterset_fields = ['party_id']


class UserViewSet(viewsets.ModelViewSet):
    """
    UserViewSet:
        Returns a list of all **users** in the system.
        Uses the **UserSerializer** as serializer class.
        Lookup the **username** field to search between all the elements.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['username']
