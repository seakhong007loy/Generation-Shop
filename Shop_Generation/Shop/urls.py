from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='home', view=views.home, name='home'),
    path(route='bags', view=views.bags , name='bags'),
    path(route='detail_bags/<int:id>',view=views.detail_bags, name='detail_bags')

]