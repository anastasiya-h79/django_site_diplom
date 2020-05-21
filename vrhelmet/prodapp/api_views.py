from django.conf.urls import url, include
from .models import Category, Helmets
from .serializers import CategorySerializer, HelmetsSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser
from .permissions import ReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication

class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class HelmetsViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Helmets.objects.filter(is_active=True)
    serializer_class = HelmetsSerializer
