from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from django.forms import FileInput

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("Username already registered")
        return data

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']


    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already registered")
        return data


class UserEditForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email')

  def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Email already registered")
        return data
  
  def clean_username(self):
        data = self.cleaned_data['username']
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("Username already registered")
        return data
  
  
class ProfileEditForm(forms.ModelForm):
  avatar = forms.ImageField(widget=FileInput)
  class Meta:
    model = Profile
    fields = ('avatar', )

  
  def clean_avatar(self):
        file = self.cleaned_data.get('avatar')
        valid_extensions = ['png', 'jpg', 'jpeg', 'ico']  # добавьте нужные расширения
        ext = file.name.split('.')[-1].lower()
        if ext not in valid_extensions:
          raise ValidationError('Insert a picture')
        
        return file
