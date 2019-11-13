from django.forms import ModelForm
from .models import Bb
from django import forms
class BbForm(ModelForm):
  class Meta:
    model = Bb
    fields = ('title','content','price','rubric')

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

