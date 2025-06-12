from django.contrib import admin
from .models import Sisan

# Register your models here.
@admin.register(Sisan)
class SisanAdmin(admin.ModelAdmin):
    pass