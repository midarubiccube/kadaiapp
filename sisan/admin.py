from django.contrib import admin
from .models import Sisan, Department

# Register your models here.
@admin.register(Sisan)
class SisanAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass