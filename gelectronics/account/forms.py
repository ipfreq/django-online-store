from django import forms
from gelectronics import settings
from django.contrib.auth.models import User
from .models import Account
from shop.models import Product


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class UserRegForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password1=forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','first_name','email')

    def clean_password1(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password1']:
            raise forms.ValidationError('Passwords doesn\'t match')
        return cd['password1']

class AccountRegForm(forms.ModelForm):
    birth_date=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model=Account
        fields=('dp_image','birth_date')

class EditUser(forms.ModelForm):
    class Meta :
        model=User
        fields=('first_name','email')


class EditAccount(forms.ModelForm):
    birth_date=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)

    class Meta:
        model=Account
        fields=('dp_image','birth_date')
