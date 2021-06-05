from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.


def index(request):
    products = Products.objects.all()
    
    return render(request,  'ecom/index.html',  {"products" : products})
    
def details(request, id):
    productid = id
    product = Products.objects.get(id=productid)
    return render (request, 'ecom/detail.html',  {'product':product})