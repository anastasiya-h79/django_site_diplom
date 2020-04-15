from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from django.shortcuts import get_list_or_404

from .models import Helmets, Category, Carusel, Message
from .forms import ContactForm, Contacts
from django.core.mail import send_mail

# Create your views here.

# def main_view(request):      #request не импортируем, но передаем
#     helmets = Helmets.objects.all()                   #будет запрос к БД
#     category = Category.objects.all()
#     carus = Carusel.objects.get()
#     #print(type(carus))
#     return render(request, 'prodapp/index.html', context={'category': category, 'helmets': helmets, 'carus': carus})    #request - чтобы данные запроса попали в шаблон

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
        context.update ({'category': category, 'carus': carus})
        return context


class MainListView(ListView, DateContextMixin):
    model = Helmets
    template_name = 'prodapp/index.html'


def contacts(request):
    return render(request, 'prodapp/contact.html')

# def contactform(request):
#     if request.method == 'POST':
#         contactform = ContactForm(request.POST)
#         if contactform.is_valid():
#             # Получить данные из форы
#             name = contactform.cleaned_data['name']
#             message = contactform.cleaned_data['message']
#             email = contactform.cleaned_data['email']
#
#             send_mail(
#                 'Contact message',
#                 f'Ваше сообщение {message} принято',
#                 'from@example.com',
#                 [email],
#                 fail_silently=True,
#             )
#
#             return HttpResponseRedirect(reverse('prodapp:index'))
#         else:
#             return render(request, 'prodapp/contactform.html', context={'contactform': contactform})
#     else:
#         contactform = ContactForm()
#         return render(request, 'prodapp/contactform.html', context={'contactform': contactform})

class ContactFormCreateView(CreateView, DateContextMixin):
    fields = '__all__'
    model = Message
    success_url = reverse_lazy('prodapp:index')
    template_name = 'prodapp/contactform.html'

    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


# def card(request, id):
#     card = get_object_or_404(Helmets, id=id)
#     #card = Helmets.objects.get(id=id)
#     category = Category.objects.all()
#     return render(request, 'prodapp/card.html', context={'category': category, 'card': card})

class CardDetailView(DetailView, DateContextMixin):
    model = Helmets
    template_name = 'prodapp/card.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Helmets, id=self.id)


class StandaloneListView(ListView, DateContextMixin):
    model = Helmets
    template_name = 'prodapp/helmets_category.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.cat_id = kwargs['pk']
        #Helmets.objects.filter(category__id=self.cat_id)
        return super().get(request, *args, **kwargs)
        #return Helmets.objects.filter(Helmets, category__id=self.cat_id)

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Helmets.objects.filter(category__id=self.cat_id )
        #return Category.objects.filter(Category, cat_id=self.cat_id)