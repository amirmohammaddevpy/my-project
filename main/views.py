from django.shortcuts import render ,get_object_or_404
from .models import MyProject

# Create your views here.
def home(request):
    project = MyProject.objects.all()
    return render(request,"home/home.html",{'projects':project})

def detail(request,name):
    project = get_object_or_404(MyProject,name=name)
    return render(request,'home/detail.html',{'project':project})

def anout_me(request):
    return render(request,'home/about_me.html')