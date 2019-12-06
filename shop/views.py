from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    product = Product.objects.all()
    n = len(product)
    n_side = n//4 + ceil(n/4 - n//4)
    print('**********'+str(range(1,n_side)))
    params = {'product':product, 'n_side':n_side, 'range' : range(1,n_side)}
    return render(request,'shop/index.html', params)

def contact(request):
    return HttpResponse("contact us")

def about(request):
    params = []
    return render(request,'shop/about.html',params)

def ProductView(request):
    params=[]
    return HttpResponse("product view")

def tracker(request):
    return HttpResponse("tracking product delivery.")
