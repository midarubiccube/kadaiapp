from django.urls import path
from . import views

app_name = 'sisan'
urlpatterns = [
    path('', views.index, name='index'),
]
