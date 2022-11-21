from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('user','comment','sitterProfile',)
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-coontrol', 'placeholder':'Comment Here'}),
            'sitterProfile': forms.HiddenInput()
        }
    