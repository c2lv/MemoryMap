from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
