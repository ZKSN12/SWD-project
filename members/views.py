from django.contrib.auth.models import User
from rest_framework import status

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from time import time

from django.http import JsonResponse
from django.forms.models import model_to_dict
from petsitterapp.models import SitterProfile
from .forms import PetForm
from .models import PetInfo
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


def register(request):
    username = request.POST.get('username')
    if username is None:
        return render(request, "authenticate/register.html")

    password = request.POST.get('password')
    password_repeat = request.POST.get('password-repeat')
    # password check to be done in frontend
    user_email = request.POST.get('email')

    if User.objects.filter(username=username).count() != 0:
        print('Username already exist.')
        # return JsonResponseError('Username already exist.')
        return render(request, "authenticate/register.html")

    user = User(username=username, email=user_email)
    user.set_password(password)
    user.save()

    login(request, user)
    return redirect('yourpage')


# @csrf_exempt
@login_required(login_url='user-login')
def get_user_profile(request):
    if not request.user.is_authenticated:
        return JsonResponseError('Invalid user identity.')

    user = User.objects.get(username=request.user.username)
    context = {
        'username': user.username,
        'user_email': user.email,
        'login_time': user.last_login
    }
    print(context)

    return render(request, 'yourpage', context)


def jason(request):
    sitters= SitterProfile.objects.filter(name="jason")
    return render(request, 'petsitterapp/JasonProfile.html', {'sitters':sitters})


@login_required(login_url='login')
def yourpage(request):
    if not request.user.is_authenticated:
        return JsonResponseError('Invalid user identity.')

    user = User.objects.get(username=request.user.username)

    pet_list = PetInfo.objects.all()

    context = {
        'user_info': {
            'username': user.username,
            'email': user.email,
            'login_time': user.last_login
        },
        'pet_list': pet_list,

    }
    return render(request, 'authenticate/yourpage.html', context)



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


# Json response converter
def JsonResponseOK(data=None):
    return JsonResponse({
        'success': True,
        'data': data,
        'message': 'ok'
    }, status=status.HTTP_200_OK)


# Json response converter
def JsonResponseError(message: str, error=None, status: int = status.HTTP_400_BAD_REQUEST):
    return JsonResponse({
        'success': False,
        'message': message,
        'error': error
    }, status=status)
