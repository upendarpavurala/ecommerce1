from django import forms
from django.forms import ModelForm

from .models import Signup
class SignUpForm(ModelForm):
    class Meta:
        model=Signup
        widgets={'password':forms.PasswordInput(),
                 'rpsw':forms.PasswordInput()}
        fields=['firstname','lastname','username','phone_no','email','password','rpsw']


class SignInForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput())

