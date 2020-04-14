from django import forms
from .models import Helmets
from .models import Category

class Contacts(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(label='email',
                            widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
    message = forms.CharField(label='Введите сообщение', widget=forms.TextInput(attrs={'placeholder': 'email', 'class': 'form-control'}))

    # Чекбоксы
    #tags = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple())


    class Meta:
        model = Helmets
        fields = '__all__'
        # fields = ('name', 'category')
        # exclude = ('category',)