# forms.py
from django import forms
from .models import UserForm

class UserFormModelForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['name', 'mail', 'phno', 'rent', 'city', 'university']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'phno': forms.TextInput(attrs={'class': 'form-control'}),
            'rent': forms.NumberInput(attrs={'class': 'form-control'}),
            'university': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
        }

