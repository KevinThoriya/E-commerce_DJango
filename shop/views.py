from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html',)

def contact(request):
    return HttpResponse("contact us")

def about(request):
    return render(request,'shop/about.html',)

def ProductView(request):
    return HttpResponse("product view")

def tracker(request):
    return HttpResponse("tracking product delivery.")