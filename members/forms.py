from django import forms
from django.forms import ModelForm
from .models import PetInfo



class PetForm(ModelForm):
    class Meta:
        model = PetInfo
        fields = ('info', 'pic', 'introduction')
        widgets = {
            'info': forms.TextInput(attrs={'placeholder':'pet type and age'}),
            'introduction': forms.TextInput(attrs={'placeholder':'an introduction of your pet'}),
        }
    
