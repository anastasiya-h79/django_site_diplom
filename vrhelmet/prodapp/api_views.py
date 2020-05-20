from django.conf.urls import url, include
from .models import Category, Helmets
from .serializers import CategorySerializer, HelmetsSerializer
from rest_framework import routers, serializers, viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HelmetsViewSet(viewsets.ModelViewSet):
    queryset = Helmets.objects.filter(is_active=True)
    serializer_class = HelmetsSerializer
