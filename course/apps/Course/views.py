from django.shortcuts import render,redirect
from models import Coursenames, Descriptions
# Create your views here.
def index(request):
    context={
        "Coursenames":Coursenames.objects.all()
        }
    return render(request,'Course/index.html',context)

def courses(request):
    course = Coursenames.objects.create( title=request.POST['title'])
    Descriptions.objects.create( decription=request.POST['decription'], course=course)
    return redirect('/')


def review(request, id):
    context = {
        'Coursename':Coursenames.objects.all().filter(id=id)
        }
    return render(request,'Course/destroy.html',context)

def destroy(request, id):
    Coursenames.objects.get(id=id).delete()
    return redirect('/')
