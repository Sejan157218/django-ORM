from django.urls import path
from . import views

app_name = 'modelInheritance'

urlpatterns = [
    path('', views.BaseItem, name='baseItem'),
]