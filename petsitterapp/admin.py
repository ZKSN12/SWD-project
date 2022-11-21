from django.contrib import admin

from .models import SitterProfile
from .models import Comment

# Register your models here.

admin.site.register(SitterProfile)
admin.site.register(Comment)
