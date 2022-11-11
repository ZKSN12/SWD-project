from django.contrib import admin

from .models import Reviews
from .models import SitterProfile

# Register your models here.

admin.site.register(Reviews)
admin.site.register(SitterProfile)
