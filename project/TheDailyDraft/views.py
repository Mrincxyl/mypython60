from django.shortcuts import render

def MyHome(request):
    return render(request,'home.html')

def Login(request):
    return render(request,'login.html')

def Register(request):
    return render(request,'register.html')

def About(request):
    return render(request,'about.html')