from django.shortcuts import render, HttpResponse
from .models import Clothes
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')
def clothes(request):
    cl=Clothes.objects.all()
    return render(request=request, template_name='clothes.html', context={'clothes':cl})
def view(request, id):
    vw=Clothes.objects.get(id=id)
    return render (request=request, template_name='view.html', context={'view':vw})