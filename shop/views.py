from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
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
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        disc = request.POST.get('disc','')
        contact = Contact(name = name , email = email , phone = phone , disc = disc )
        contact.save()
        print(contact)
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

def checkout(request):
    params = {"range": range(0,9)}
    if request.method == "POST":
        items_cart = request.POST.get("items")
        items_cart = json.loads(items_cart)
        items = []
        for i,j in items_cart.items():
            items_id = i.replace('pr','')
            item = Product.objects.filter(id=items_id)
            product = []
            product.append(item[0].product_image)
            product.append(item[0].product_name)
            product.append(item[0].product_prize)
            product.append(j)
            product.append(j * item[0].product_prize)
            product.append(items_id)
            items.append(product)
            print(product)
        params["items"] = items
    return render(request,'shop/checkout.html',params)

def payment(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        add1 = request.POST.get("add1")
        add2 = request.POST.get("add2")
        zipcode = request.POST.get("zip_code")
        city = request.POST.get("city")
        state = request.POST.get("state")
        items = request.POST.get("items")
        order = Order(ord_name = name , ord_email = email, ord_city = city, ord_state = state , ord_add1 = add1 , ord_add2 = add2 , ord_zip = zipcode, ord_items = items )
        order.save()
        done = True
        if done :
            stmt = 'your Order has been placed. we are working on it.'
            orderupdate = OrderUpdate(orderId= order.ord_id, orderDisc=stmt, )
            orderupdate.save();
            params = {'done': done, 'id' : order.ord_id}
            return render(request,'shop/payment.html',params)
        else:
            return HttpResponse('try again after some time. sesver problem ')

def tracker(request):
    params = {}
    if request.method == 'POST':
        email = request.POST.get('email','')
        orderId = request.POST.get('orderId','')
        print(email , orderId)
        try: 
            update = Order.objects.filter(ord_email = email , ord_id = orderId)
            if len(update) > 0:
                ord_update = OrderUpdate.objects.filter(orderId = orderId)
                updates = []
                for i in ord_update:
                    updates.append({'text': i.orderDisc , 'time' : i.orderUpTime});
                responce = json.dumps(updates, default=str);
                return HttpResponse(responce);
            else:
                return HttpResponse(" {}");
        except Exception as e:
            return HttpResponse({});
    return render(request,'shop/tracker.html',params)

def search(request):
    params = {}
    return render(request,'shop/search.html',params)


