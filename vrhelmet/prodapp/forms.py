from django import forms
from .models import Helmets, Message


class Contacts(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class ContactForm(forms.ModelForm):
    # name = forms.CharField(label='Имя',
    #                        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    # email = forms.EmailField(label='Email',
    #                         widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
    # tel = forms.CharField(label='Телефон',
    #                       widget=forms.TextInput(attrs={'placeholder': 'phone', 'class': 'form-control'}))
    # message = forms.CharField(label='Введите сообщение', widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}))

    # Чекбоксы
    #tags = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Message
        fields = '__all__'
        # fields = ('name', 'category')
        # exclude = ('category',)