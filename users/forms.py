from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from users.models import Member


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    cms_id = forms.CharField()


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        cms_id = cleaned_data.get('cms_id')

        if User.objects.filter(username=username).exists():
            self.add_error('username', 'Username already exists')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email already exists')
        if Member.objects.filter(cms_id=cms_id).exists():
            self.add_error('cms_id', 'Cms ID already exists')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if not User.objects.filter(username=username).exists():
            self.add_error('username', 'Username does not exist')
