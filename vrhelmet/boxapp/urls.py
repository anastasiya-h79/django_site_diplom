from django.urls import path
from boxapp import views

app_name = 'boxapp'

urlpatterns = [
    path('order/', views.OrderListView.as_view(), name='order'),
    #path('contact/', views.contacts, name='contact'),



]