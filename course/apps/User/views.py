from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# Create your views here.

def index(request):
    return render(request, 'User/create.html')

def register(request):
    return render(request, 'User/create.html')

def login(request):
    request.session['user'] = {
        'user_id':user.id,
        'first_name':user.first_name
    }
    return render(Course, '/Course/index.html')

def logoff(request):
    request.session.clear()
    return redirect('User/create.html')
