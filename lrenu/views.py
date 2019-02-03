from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def forgotPasswd(request):
    return render(request, 'forgot-password.html')