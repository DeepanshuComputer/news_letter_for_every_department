
from django.shortcuts import get_object_or_404, render ,redirect
from django.http import HttpResponse
from .forms import Subs_Form , News_Form
from .models import *
from django.contrib.auth.decorators import login_required


from email.message import EmailMessage
import ssl
import smtplib
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def Send_Mail(recipient,subject,body):
    sender="ppkkcc2@gmail.com"
    em=EmailMessage()
    em['From']=sender
    em['To']=recipient
    em['Subject']=subject
    em.set_content(body)
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,"mjecctipucnrebkq")
        smtp.sendmail(sender,recipient,em.as_string())
def home(request):
    
    obj=department_cat.objects.all()
    all_news = news.objects.all()
    print(obj)
    return render(request, 'Headline_Express/home.html',{'obj':obj,"all_news":all_news})

def Subscribe(request):
    if request.method == 'GET':
        x=Subs_Form()
        return render(request, 'Headline_Express/Subscribe.html',{"form":x})
    else:
        x=Subs_Form()
        data=Subs_Form(request.POST)
        if data.is_valid():
            data.save()
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


def all_news(request):
    all_news = news.objects.all()
    return render(request, 'Headline_Express/all_news.html',{"all_news": all_news})


def news_category(request):
    return render(request, 'Headline_Express/news_category.html')
    
def news_category(request):
    obj=department_cat.objects.all()
    print(obj)
    return render(request, 'Headline_Express/news_category.html',{'obj':obj})



@login_required
def Post_news_letter(request):
    x=News_Form()
    if request.method == 'GET':
        x=News_Form()
        return render(request, 'Headline_Express/Post_news_letter.html',{"News_Form":x})
    else:
        y=subs_info.objects.all()
        
        
        data=News_Form(request.POST , request.FILES)
        if data.is_valid():
             for y in y:
                 
                 body=f"Hello Dear {y.Name}\nNew NewsLetter Arrived Please Check it out"
                 Send_Mail(y.Email,"New NewsLetter Arrived",body)
                 print("Mail sent successfully")
            
             print(data)
             data.save()
             print(data)
             return render(request, 'Headline_Express/Post_news_letter.html',{"News_Form":x})
        else:
            return render(request, 'Headline_Express/Post_news_letter.html',{"News_Form":x})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'myblogs/loginuser.html', {'form':AuthenticationForm()})
    else:
        a= request.POST.get('username') 
        b= request.POST.get('password') 
        user =authenticate(request,username=a,password=b)
        if user is None:
            return render(request,'Headline_Express/loginuser.html',{'form':AuthenticationForm(), 'error':'Invalid  Credentials'})
        else :
            login(request, user)
            return redirect('home')



def signupuser(request):
    if request.method =='GET':
        return render(request,'Headline_Express/signupuser.html',{'form':UserCreationForm()})
    else:
        a= request.POST.get('username') 
        b= request.POST.get('password1') 
        c= request.POST.get('password2') 
        if b==c:
            # check whether user name is unique
            if (User.objects.filter(username =a)):
                return render(request,'Headline_Express/signupuser.html',{'form':UserCreationForm(),'error': 'User Name  Already exists Try Again'})
            else :
                user =User.objects.create_user(username =a , password=b)
                user.save()
                login(request,user)
                return redirect('home')
        else:
            return render(request,'Headline_Express/signupuser.html',{'form':UserCreationForm(),'error': 'password Mismatch Try Again'})

def logoutuser(request):
    if request.method =='GET':
        logout(request)
        return redirect('home')




def about_us(request):
    return render(request, 'Headline_Express/about_us.html')

