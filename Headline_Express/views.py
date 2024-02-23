from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .forms import Subs_Form 
from .models import *

# Create your views here.


def home(request):
    obj=department_cat.objects.all()
    print(obj)
    return render(request, 'Headline_Express/home.html',{'obj':obj})

def Subscribe(request):
    x=Subs_Form()
    if request.method == 'GET':
        return render(request, 'Headline_Express/Subscribe.html',{"form":x})
    else:
        x=Subs_Form(request.POST)
        if x.is_valid():
            x.save()
            return render(request, 'Headline_Express/Subscribe.html',{"form":x})
        else:
            return render(request, 'Headline_Express/Subscribe.html',{"form":x})
        
def dep_cat(request):
    a=request.GET.get('id')
    x=get_object_or_404(department_cat,pk=a)
    obj1=departments.objects.filter(main_dep__main_dep=x.main_dep)
    
    print(obj1)
    return render(request, 'Headline_Express/dep_cat.html',{"obj": obj1})


def dep_cat_news(request):
    b=request.GET.get('id')
    z=get_object_or_404(departments,pk=b)
    obj2=news.objects.filter(dept_name__dept_name=z.dept_name)
    print(obj2)
    return render(request, 'Headline_Express/dep_cat_news.html',{"obj": obj2})


def news_letter(request):
    c=request.GET.get('id')
    y=get_object_or_404(news,pk=c)
    return render(request, 'Headline_Express/news_letter.html',{"y": y })
    
