from django import forms
from .models import Reg
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    email= forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = Reg
        fields = ('dp','email', 'phone_no','address','city','state','zipcode','job')

class PasswordForm(forms.ModelForm):

    class Meta:
        model = Reg
        fields = ()
