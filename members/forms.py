from django import forms
from django.forms import ModelForm
from .models import PetInfo
from .models import Tags


class PetForm(ModelForm):
    class Meta:
        model = PetInfo
        fields = ('info', 'pic', 'introduction')
        widgets = {
            'info': forms.TextInput(attrs={'class':'form-coontrol', 'placeholder':'pet type and age'}),
            'introduction': forms.TextInput(attrs={'class':'form-coontrol', 'placeholder':'an introduction of your pet'}),
        }
    
class TagForm(ModelForm):
    class Meta:
        model = Tags
        fields = ('tag',)
        widgets = {
            'tag': forms.TextInput(attrs={'class':'form-coontrol'}),
            
        }