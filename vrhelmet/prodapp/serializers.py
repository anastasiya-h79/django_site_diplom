from django.conf.urls import url, include
from .models import Category, Helmets
from rest_framework import serializers

# Serializers define the API representation.
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class HelmetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Helmets
        fields = '__all__'