from django.test import TestCase
from .models import CustomUser


class GameViewTest(TestCase):
    @classmethod
    def setUp(self):
        test_user1 = CustomUser.objects.create_user(username='testuser1', email='testuser1@test.com', password='testuser1')
        test_user1.save()

    def test_return_unauthorized(self):
        response = self.client.get('/api/games/')
        self.assertEqual(response.status_code, 401)

    def test_logged_user(self):
        login = self.client.login(username='testuser1', password='testuser1')
        response = self.client.get('/api/games/')

        self.assertEqual(response.status_code, 200)


class PartyViewTest(TestCase):
    @classmethod
    def setUp(self):
        test_user1 = CustomUser.objects.create_user(username='testuser1', email='testuser1@test.com', password='testuser1')
        test_user1.save()

    def test_return_unauthorized(self):
        response = self.client.get('/api/parties/')
        self.assertEqual(response.status_code, 401)

    def test_logged_user(self):
        login = self.client.login(username='testuser1', password='testuser1')
        response = self.client.get('/api/parties/')

        self.assertEqual(response.status_code, 200)


class MessageViewTest(TestCase):
    @classmethod
    def setUp(self):
        test_user1 = CustomUser.objects.create_user(username='testuser1', email='testuser1@test.com', password='testuser1')
        test_user1.save()

    def test_return_unauthorized(self):
        response = self.client.get('/api/messages/')
        self.assertEqual(response.status_code, 401)

    def test_logged_user(self):
        login = self.client.login(username='testuser1', password='testuser1')
        response = self.client.get('/api/messages/')

        self.assertEqual(response.status_code, 200)
