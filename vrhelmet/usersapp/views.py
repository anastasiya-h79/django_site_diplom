from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic.base import ContextMixin

from .forms import RegistrationForm
from django.views.generic import CreateView, DetailView
from .models import SiteUser
from prodapp.models import Helmets, Category, Carusel, Message
from rest_framework.authtoken.models import Token

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

class UserDetailView(DetailView):
    template_name = 'usersapp/profile.html'
    model = SiteUser


def update_token(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        # создать
        Token.objects.create(user=user)
    return HttpResponseRedirect(reverse('users:profile', kwargs={'pk': user.pk}))


def update_token_ajax(request):
    user = request.user
    # если уже есть
    if user.auth_token:
        # обновить
        user.auth_token.delete()
        token = Token.objects.create(user=user)
    else:
        # создать
        token = Token.objects.create(user=user)
    return JsonResponse({'key': token.key})
