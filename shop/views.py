from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    allprod = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        n_slide = n//4 + ceil(n/4 - n//4)
        allprod.append([prod , range(1,n_slide), n_slide])
    params = {'allprod':allprod,}
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
