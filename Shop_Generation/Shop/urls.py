from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='home', view=views.home, name='home'),
    path(route='clothes', view=views.clothes, name='clothes'),
    path('view/<int:id>', view=views.view, name='view')
]