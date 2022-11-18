from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sitter/', views.sitter, name ='sitter'),
    path('jason/', views.jason, name ='jason'),
    path('sam/', views.sam, name ='sam'),
    path('laura/', views.laura, name ='laura'),
    path('chris/', views.chris, name ='chris'),
    path('ashley/', views.ashley, name ='ashley'),
    path('about/', views.about, name ='about'),
    
]