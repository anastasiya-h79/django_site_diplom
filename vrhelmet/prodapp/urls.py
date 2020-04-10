from django.urls import path
from prodapp import views

app_name = 'prodapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('contact/', views.contacts, name='contact'),
    path('card/<int:id>/', views.card, name='card'),
    path('contactform/', views.contactform, name='contactform')


]