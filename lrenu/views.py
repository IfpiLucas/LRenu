from django.shortcuts import render
from .models import *
from .form import *

def index(request):
    data = {}
    data['util'] = User.objects.all()
    return render(request, 'index.html', data)

def login(request):
    return render(request, 'login.html')

def register(request):
    form = UserForm()
    if form.is_valid():
        form.save()
    return render(request, 'register.html', {'form': form})

def forgotPasswd(request):
    return render(request, 'forgot-password.html')

def contatos(request):
    data = {}
    return render('list.html', data)