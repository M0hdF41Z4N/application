from django import forms
from .models import Lead
from django.forms import ModelForm

class LeadCreateForm(ModelForm):
    class Meta:
        model = Lead
        exclude = ['id,created_on,lead_status']

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control"
            }
        ))
