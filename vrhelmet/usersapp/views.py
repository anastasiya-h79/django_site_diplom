from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin

from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import SiteUser
from prodapp.models import Helmets, Category, Carusel, Message

class DateContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        category = Category.objects.all()
        carus = Carusel.objects.get()
        context.update({'category': category, 'carus': carus})
        return context
# Create your views here.
class UserLoginView(LoginView, DateContextMixin):
    template_name = 'usersapp/login.html'

class UserCreateView(CreateView, DateContextMixin):
    model = SiteUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')

class ManagerCreateView(CreateView, DateContextMixin):
    model = SiteUser
    template_name = 'usersapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')
