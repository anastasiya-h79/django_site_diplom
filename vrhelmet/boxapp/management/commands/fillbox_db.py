from django.core.management.base import BaseCommand
from boxapp.models import Methodpay, Delivery, Userinfo, Order



class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Hello box')