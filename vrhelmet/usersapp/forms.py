
from django.contrib.auth.forms import UserCreationForm
from .models import SiteUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = SiteUser
        fields = ('username', 'phone', 'password1', 'password2')
        # help_texts = {
        #     'username': None,
        #     'phone': None,
        #     'password1': None,
        #     'password2': None
        # }
