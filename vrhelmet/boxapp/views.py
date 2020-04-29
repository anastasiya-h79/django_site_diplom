from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_list_or_404

from .models import ProductInOrder, UserInfo, Delivery, MethodPay
from prodapp.views import DateContextMixin


# Create your views here.
# вьюшка для корзины заказа с правами для залогиненного текущего пользователя
class OrderListView(LoginRequiredMixin, ListView, DateContextMixin):
    model = ProductInOrder
    template_name = 'boxapp/order.html'

    def test_func(self):
        return self.request.user