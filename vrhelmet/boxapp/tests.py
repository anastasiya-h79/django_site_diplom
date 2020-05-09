from django.test import TestCase
from mixer.backend.django import mixer
from faker import Faker

from .models import *
from prodapp.models import Helmets, Category

# Create your tests here.
class MethodPayTestCase(TestCase):
    def setUp(self):
        self.methodpay = MethodPay.objects.create(name='test_methodpay')

    def test_str(self):
        self.assertEqual(str(self.methodpay), 'test_methodpay')


class DeliveryTestCase(TestCase):
    def setUp(self):
        self.delivery = Delivery.objects.create(name='test_delivery')

    def test_str(self):
        self.assertEqual(str(self.delivery), 'test_delivery')


class StatusTestCase(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name='test_status')

    def test_str(self):
        self.assertEqual(str(self.status), 'Статус test_status')


class UserInfoTestCaseFaker(TestCase):
    def setUp(self):
        faker = Faker()
        self.userinfo = UserInfo.objects.create(name=faker.name(), surname=faker.name(),
                                              email='test_email', comment=faker.name())
        self.userinfo_str = UserInfo.objects.create(name='test_name')

    def test_str(self):
        self.assertEqual(str(self.userinfo_str), 'test_name')


class ProductInOrderTestCase(TestCase):

    def setUp(self):
        nmb = 3
        deliveryprice = 200
        price_per_item = 1000
        methodpay = MethodPay.objects.create(name='test_methodpay')
        delivery = Delivery.objects.create(name='test_delivery')
        status = Status.objects.create(name='test_status')
        order = Order.objects.create(total_price=3000, status=status)
        category = Category.objects.create(name='test_category')
        price = 0
        product = Helmets.objects.create(name='test_product_name', category=category, description='something',
                                             price=price, stock='test_stock', guarantee='test_guarantee')

        self.productinorder = ProductInOrder.objects.create(order=order, product=product, deliveryprice=deliveryprice,
                                                            nmb=nmb, methodpay=methodpay, delivery=delivery, price_per_item=price_per_item)

    def test_str(self):
        self.assertEqual(str(self.productinorder), 'test_product_name')
