from django.shortcuts import render, HttpResponse
from .models import Clothes
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')
