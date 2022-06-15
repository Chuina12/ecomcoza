from email import message
import re
from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import messages
from . form import UserForm

def index(request):
    return render(request, 'user/index.html')


def log(request):
    return render(request, 'user/login.html')

  
def loguser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'connexion reussie !')
            return redirect('blog')
        else:
            messages.error(request, 'echec de connexion')
            
    return render(request, 'user/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'your account has been created')
    else:
        messages.error(request, form.errors)
    return render(request, 'user/register.html', {'form':form})

def blog(request):
    return render(request, 'user/blog.html')

def account(request):
    return render(request, 'user/account.html')