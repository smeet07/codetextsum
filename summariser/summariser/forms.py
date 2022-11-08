from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TextSum,PythonSum
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class TextSumForm(forms.ModelForm):
    class Meta:
        model=TextSum
        fields=['text']
class PySumForm(forms.ModelForm):
    class Meta:
        model=PythonSum
        fields=['code']