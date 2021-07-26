from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from clg.models import Permission,Payment

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[ 'username','email','password1','password2']

class PermissionForm(forms.ModelForm):
    class Meta:
        model=Permission
        fields='__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields='__all__'