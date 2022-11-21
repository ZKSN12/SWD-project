from django.urls import path
from .views import sitterView,ProfileDetailView


from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sitter/',sitterView.as_view(), name='sitter'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
    path('about/', views.about, name ='about'),
    
]