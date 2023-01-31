from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    '''Custom form that extends the UserCreationForm to add mail'''
    email = forms.EmailField(required=True)

    class Meta:
        '''config'''
        model = User
        fields = ['username', 'email', 'password1', 'password2']