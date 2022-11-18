from django.shortcuts import render
from .models import SitterProfile
from .models import Reviews


# Create your views here.

def base(request):
    return render(request, 'petsitterapp/base.html', {})

def index(request):
    return render(request, 'petsitterapp/index.html', {})

def sitter(request):
    sitter_list = SitterProfile.objects.all()
    return render(request, 'petsitterapp/SitterPage.html', {'sitter_list': sitter_list})

def jason(request):
    reviews = Reviews.objects.all()
    sitters= SitterProfile.objects.filter(name="jason")
    return render(request, 'petsitterapp/JasonProfile.html', {'sitters':sitters, 'reviews':reviews})

def sam(request):
    reviews = Reviews.objects.all()
    sitters= SitterProfile.objects.filter(name="sam")
    return render(request, 'petsitterapp/SamProfile.html', {'sitters':sitters, 'reviews':reviews})

def laura(request):
    return render(request, 'petsitterapp/LauraProfile.html', {})

def chris(request):
    return render(request, 'petsitterapp/ChrisProfile.html', {})

def ashley(request):
    return render(request, 'petsitterapp/AshleyProfile.html', {})

def about(request):
    return render(request, 'petsitterapp/about.html', {})

