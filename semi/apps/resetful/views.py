from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Product

from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'all_products':Product.objects.all()
    }
    return render(request, 'resetful/index.html',context)

def show_product(request,id):
    context={
       'product':Product.objects.get(id=id)
    }
    return render(request,'resetful/show_product.html',context)

def edit_product(request,id):
    context={
       'product':Product.objects.get(id=id)
    }
    return render(request, 'resetful/edit_product.html',context)

def add_product(request):
    return render(request,'resetful/add_product.html')

def edit_exit_product(request,id):
    Product.objects.product_edit(request.POST, id)
    return redirect(reverse('index'))

def remove_product(request,id):
    Product.objects.get(id=id).delete()
    return redirect(reverse('index'))

def create_product(request):
    response = Product.objects.product_check(request.POST)
    if not response['status']:
        for error in response['errors']:
            messages.error(request, error)
    return redirect(reverse('add_product'))

def delete(request):
    Product.objects.all().delete()
    return redirect(reverse('index'))
