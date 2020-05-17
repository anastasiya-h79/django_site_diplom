from django.test import TestCase
from mixer.backend.django import mixer
from faker import Faker

from .models import Category, Helmets, Message


# Create your tests here.
class HelmetsTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='test_category')
        price = 0
        self.helmet = Helmets.objects.create(name='test_helmet', category=category, description='something',
                                             price=price, stock='test_stock', guarantee='test_guarantee')

    def test_str(self):
        self.assertEqual(str(self.helmet), '0, test_helmet, test_category')


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='test_category')

    def test_str(self):
        self.assertEqual(str(self.category), 'test_category')

class MessageTestCase(TestCase):
    def setUp(self):
        id = 3
        self.message = Message.objects.create(name='test_name', email='test_email', text='test_text')
        self.message_str = Message.objects.create(id=id, email='test_email_str')

    def test_str(self):
        self.assertEqual(str(self.message_str), '3, test_email_str')



