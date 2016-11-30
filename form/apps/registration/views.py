from django.shortcuts import render
from . form import RegistrationForm
# Create your views here.
def index(request):
    form = RegistrationForm()
    context = {
       "RegistrationForm":form
    }
    return render(request,'registration/index.html',context)
