from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='home', view=views.home, name='home'),

]