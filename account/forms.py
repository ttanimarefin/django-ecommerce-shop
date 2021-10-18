from django.forms import ModelForm, fields
from django.contrib.auth.models import User

class RegistrationForm(ModelForm):
    class Meta:
        model =User
        fields=('email','username','password1','password2',)