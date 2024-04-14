from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserMessage  

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['message']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

