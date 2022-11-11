from django.urls import path

from . import views
# from .views import YourPageView

urlpatterns = [
    
    path('yourpage/', views.yourpage, name ='yourpage'),
    path('login/', views.login_user, name ='login'),
    path('addpet/', views.addpet, name ='addpet'),
    path('logout/', views.logout_user, name ='logout'),
    path('editpet/<pet_id>', views.editpet, name ='editpet'),

    
]