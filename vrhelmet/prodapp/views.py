from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Helmets, Category
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.

def main_view(request):      #request не импортируем, но передаем
    helmets = Helmets.objects.all()                   #будет запрос к БД
    category = Category.objects.all()
    return render(request, 'prodapp/index.html', context={'category': category, 'helmets': helmets})    #request - чтобы данные запроса попали в шаблон


def contacts(request):
    return render(request, 'prodapp/contact.html')

def contactform(request):
    if request.method == 'POST':
        contactform = ContactForm( request.POST )
        if contactform.is_valid():
            # Получить данные из форы
            name = contactform.cleaned_data['name']
            message = contactform.cleaned_data['message']
            email = contactform.cleaned_data['email']

            send_mail(
                'Contact message',
                f'Ваш сообщение {message} принято',
                '',     #from@example.com
                [email],
                fail_silently=True,
            )

            return HttpResponseRedirect( reverse( 'prodapp:index' ) )
        else:
            return render( request, 'prodapp/contactform.html', context={'contactform': contactform} )
    else:
        contactform = ContactForm()
        return render(request, 'prodapp/contactform.html', context={'contactform': contactform})


def card(request, id):
    card = get_object_or_404(Helmets, id=id)
    #card = Helmets.objects.get(id=id)
    category = Category.objects.all()
    return render(request, 'prodapp/card.html', context={'category': category, 'card': card})
