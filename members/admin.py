from django.contrib import admin
from .models import PetInfo
from .models import Tags

# Register your models here.

admin.site.register(PetInfo)
admin.site.register(Tags)