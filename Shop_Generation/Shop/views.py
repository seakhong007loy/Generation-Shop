from django.shortcuts import render, HttpResponse
from django.http  import  HttpResponse
from .models import Hat
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')

def hat(request):
    h=Hat.objects.all()
    return render(request=request, template_name='hat.html', context={"list":h})

def more(request, id):
    mr=Hat.objects.get(id=id)
    return render(request=request, template_name='more.html',context={'more':mr}) 
