from django import forms
from .models import Reg
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    email= forms.CharField(max_length=100, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = Reg
        fields = ('dp','email', 'phone_no','address','city','state','zipcode','job')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = [
            'dp', 'firstname', 'lastname', 'email', 'phone_no', 'address', 'city', 'state', 'country', 'zipcode', 'job'
        ]
        widgets = {
            'dp': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'job': forms.TextInput(attrs={'class': 'form-control'}),
        }
