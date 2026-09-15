from django.shortcuts import render
# Create your views here.
from django.http import  HttpResponse
from .models import Bags
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')
def bags(request):
    bg=Bags.objects.all()
    return render (request=request, template_name='bags.html' ,context={'bags_list':bg})
def detail_bags(request,id):
    sl=Bags.objects.get(id=id)
    return render (request=request, template_name='detail_bags.html',context={'detail_bags':sl})