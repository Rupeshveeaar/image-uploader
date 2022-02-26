from django import forms
from .models import Image

from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm ,SetPasswordForm
class StudentForm(UserCreationForm):
  error_css_class='error'
  required_css_class='required'
  email=forms.EmailField(error_messages={'required':'Enter your Email'}, min_length=10 , max_length=20),

  class Meta:
     model=User
     fields=['username','email']
     labels={'email':'Email'}  
  


class Webs(PasswordChangeForm):
  new_password2=forms.CharField(label='Confirm_Password(again)',widget=forms.PasswordInput)    


class Webss(SetPasswordForm):
  new_password2=forms.CharField(label='Confirm_Password', widget=forms.PasswordInput)


class ImageForm(forms.ModelForm):
  class Meta:
    model=Image
    fields='__all__'
    labels={'photo':'Upload Image'}


     