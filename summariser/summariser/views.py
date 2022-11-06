from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import View
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
def landing(request):
    return render(request,'landing.html')
def registerPage(request):
    form=CreateUserForm
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created')
            return redirect('login')

    context={
        "form":form,
    }
    return render(request,'register.html',context)
def loginPage(request):
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           return redirect('home1')
       else :
           messages.info(request,'Username or password incorrect')
    context={}
    return render(request,'login.html',context)
def textsumPage(request):
    
    return render(request,'textsum.html')
def codesumPage(request):
    
    return render(request,'codesum.html')
