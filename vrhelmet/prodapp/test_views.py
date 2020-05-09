from django.test import Client
from django.test import TestCase
from faker import Faker
from mixer.backend.django import mixer


from usersapp.models import *
from prodapp.models import Carusel

class OpenViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.fake = Faker()
        self.carusel = mixer.blend(Carusel, image1=None, image2=None, image3=None)


    def test_statuses(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/contactform/')
        self.assertEqual(response.status_code, 200)
        # post зарос
        response = self.client.post('/contactform/',
                                     {'name': self.fake.name(), 'text': self.fake.text(),
                                      'email': self.fake.email()})

        self.assertEqual(response.status_code, 302)

    def test_login(self):
        SiteUser.objects.create_user(username='test_name', password='honyak78')
        # Ошибка ввода данных
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

        # Логиним
        self.client.login(username='test_name', password='honyak79')
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)