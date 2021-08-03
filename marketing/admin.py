from django.contrib import admin

# Register your models here.
from .models import Signup, Logo

admin.site.register(Signup)
admin.site.register(Logo)