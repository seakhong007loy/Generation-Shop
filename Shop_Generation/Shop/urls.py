from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('hat/', views.hat, name='hat'),
    path('more/<int:id>',views.more, name='more'),
    
]