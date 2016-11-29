from django.shortcuts import render,redirect
from models import Blog, Comment

# Create your views here.
def index(request):
    context={
     "Blog":Blog.objects.all()
    }
    return render(request,'ORM/index.html',context)

def blogs(request):
    #using database and ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    return redirect('/')

def comments(request,id):
    blog = Blog.objects.get(id=id)
    Comment.objects.create(comment=request.POST['comments'], blog=blog)
    return redirect('/')
