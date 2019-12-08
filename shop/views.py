from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    allprod = []
    catprods = Product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(product_category=cat)
        n = len(prod)
        n_slide = n//4 + ceil(n/4 - n//4)
        allprod.append([prod , range(1,n_slide), n_slide])
    params = {'allprod':allprod,}
    return render(request,'shop/index.html', params)

def contact(request):
    params = {}
    return render(request,'shop/contact.html',params)

def about(request):
    params = {}
    return render(request,'shop/about.html',params)

def ProductView(request, id):
    #fetch product with id
    product = Product.objects.filter(id=id)
    prodcat = product[0].product_category
    simiprod = Product.objects.filter(product_category=prodcat)
    print(simiprod)
    n = len(simiprod)
    n_slide = n//4 + ceil(n/4 - n//4)
    params = {'product':product[0], 'simiprod' : [[simiprod,range(1,n_slide), n_slide ], ] }
    return render(request,'shop/product.html',params)

def tracker(request):
    params = {}
    return render(request,'shop/tracker.html',params)

def search(request):
    params = {}
    return render(request,'shop/search.html',params)
