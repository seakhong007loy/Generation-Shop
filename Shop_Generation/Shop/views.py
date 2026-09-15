from django.shortcuts import render, HttpResponse
from .models import Shoes
# Create your views here.

def home(request):
    return render(request=request, template_name='home.html')
<<<<<<< Updated upstream
def clothes(request):
    cl=Clothes.objects.all()
    return render(request=request, template_name='clothes.html', context={'clothes':cl})
def view(request, id):
    vw=Clothes.objects.get(id=id)
    return render (request=request, template_name='view.html', context={'view':vw})
=======
def home(request):
    return render(request, template_name='home.html')

def shoeses(request):
    sh = Shoes.objects.all()
    return render(request, template_name='shoeses.html', context={'list':sh})

def shoeses_detail(request,id):
    shd =Shoes.objects.get(id=id)
    return render(request, template_name='shoeses_detail.html', context={'shoeses_detail':shd})
>>>>>>> Stashed changes
