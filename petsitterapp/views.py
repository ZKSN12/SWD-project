from django.shortcuts import redirect, render
from .models import SitterProfile
from .models import Comment
from .forms import CommentForm
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import FormMixin

from django.urls import reverse


# Create your views here.
class sitterView(ListView):
    model = SitterProfile
    template_name = 'petsitterapp/sitterprofile_list.html'
    

class ProfileDetailView(DeleteView):
    model = SitterProfile
    template_name = 'petsitterapp/profile_detail.html'


def base(request):
    return render(request, 'petsitterapp/base.html', {})

def index(request):
    return render(request, 'petsitterapp/index.html', {})

# def sitter(request):
#     sitter_list = SitterProfile.objects.all()
#     return render(request, 'petsitterapp/SitterPage.html', {'sitter_list': sitter_list})

def about(request):
    return render(request, 'petsitterapp/about.html', {})

