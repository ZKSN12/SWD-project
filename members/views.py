from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from time import time

from django.http import JsonResponse
from django.forms.models import model_to_dict
from petsitterapp.models import SitterProfile
from .forms import PetForm, TagForm
from .models import PetInfo, Tags
from django.contrib.auth.decorators import login_required
from django.views.generic import View

# Create your views here.


def login_user(request):
    if request.user.is_authenticated:
        return redirect('yourpage')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('yourpage')
            else:
                messages.success(request, ("Invalid username or password."))
                return redirect('login')

        return render(request,'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')

def jason(request):
    sitters= SitterProfile.objects.filter(name="jason")
    return render(request, 'petsitterapp/JasonProfile.html', {'sitters':sitters})

@login_required(login_url='login')
def yourpage(request):
    pet_list = PetInfo.objects.all()
    return render(request,'authenticate/yourpage.html', { 'pet_list': pet_list})



@login_required(login_url='login')
def editpet(request, pet_id):
    pet = PetInfo.objects.get(pk=pet_id)
    form = PetForm(request.POST or None, request.FILES or None, instance=pet)
    if form.is_valid():
        form.save()
        return redirect('yourpage')
    return render(request,'authenticate/editpet.html', 
    {
        'pet':pet,
        'form':form,
        })

@login_required(login_url='login')
def addpet(request):
    submitted = False
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('yourpage')
    else:
        form = PetForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'authenticate/addpet.html', {'form':form, 'submitted':submitted})

# class YourPageView(View):
#     def get(self, request):
#         tags= Tags.objects.all()
#         form = TagForm()
#         if request.is_ajax():
#             return JsonResponse({'tags':tags, 'form':form}, status=200)
#         return render(request, 'authenticate/yourpage.html',{}) 
