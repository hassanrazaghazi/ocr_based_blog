# from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Registeration


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
    else:
        context = {}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    
    return render(request, 'register.html')