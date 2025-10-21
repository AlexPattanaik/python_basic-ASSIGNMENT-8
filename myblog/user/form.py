from math import trunc

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
first_name=forms.CharField()
last_name=forms.CharField()
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        })
    )
class user (UserCreationForm):

    class Meta :
        model=User
        fields=['username','email','password1','password2','first_name','last_name']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # ✅ Add placeholders
    #     self.fields['username'].widget.attrs.update({'placeholder': 'Enter your username'})
    #     self.fields['first_name'].widget.attrs.update({'placeholder': 'Enter your first name'})
    #     self.fields['last_name'].widget.attrs.update({'placeholder': 'Enter your last name'})
    #     self.fields['email'].widget.attrs.update({'placeholder': 'Enter your email address'})
    #     self.fields['password1'].widget.attrs.update({'placeholder': 'Enter your password'})
    #     self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm your password'})

    def save(self, commit = True):
        user=super().save(commit=False)
        user.is_staff=True
        user.is_superuser=True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
