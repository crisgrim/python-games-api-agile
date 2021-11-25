from django.test import TestCase
from .models import CustomUser, Game, Party, Message


class GameTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(email='test3@test.com', username='Test3', password='test3')
        user.save()
        game = Game.objects.create(name='Fallout', added_by=user)
        game.save()

    def test_game_name(self):
        game = Game.objects.get(id=1)
        name = game.name
        self.assertEqual(name, 'Fallout')

    def test_game_name_max_length(self):
        game = Game.objects.get(id=1)
        max_length = game._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)


class PartyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(email='test3@test.com', username='Test3', password='test3')
        user.save()
        game = Game.objects.create(name='Fallout', added_by=user)
        game.save()
        party = Party.objects.create(name='Alpha team', game_id=game, added_by=user)
        party.save()

    def test_game_name(self):
        party = Party.objects.get(id=2)
        name = party.name
        self.assertEqual(name, 'Alpha team')

    def test_game_name_max_length(self):
        party = Party.objects.get(id=2)
        max_length = party._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)


class MessageTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = CustomUser.objects.create(email='test3@test.com', username='Test3', password='test3')
        user.save()
        game = Game.objects.create(name='Fallout', added_by=user)
        game.save()
        party = Party.objects.create(name='Alpha team', game_id=game, added_by=user)
        party.save()
        message = Message.objects.create(content='Hello? Somebody to play today?', party_id=party, added_by=user)
        message.save()

    def test_game_name(self):
        message = Message.objects.get(id=1)
        content = message.content
        self.assertEqual(content, 'Hello? Somebody to play today?')

    def test_game_name_max_length(self):
        message = Message.objects.get(id=1)
        max_length = message._meta.get_field('content').max_length
        self.assertEqual(max_length, 100)
