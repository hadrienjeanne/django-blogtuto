from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    '''Custom form that extends the UserCreationForm to add mail'''
    email = forms.EmailField(required=True)

    class Meta:
        '''config'''
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    '''Custom form to update user profile username / email'''
    email = forms.EmailField(required=True)

    class Meta:
        '''config'''
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    '''Custom form to update user image'''
    class Meta:
        '''config'''
        model = Profile
        fields = ['image']