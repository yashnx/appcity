from email.policy import default
from django.shortcuts import render
from django.http import HttpResponse
from numpy import true_divide
from .models import Product,Order
from math import ceil
import json
from django.shortcuts import HttpResponse
import pandas as pd
from django.db.models import Q
import random
from datetime import datetime
def index(request):
    products= Product.objects.all()
    params = {'range': range(1,3),'product': products[0:6]}
    return render(request, 'shop/index.html',params)

def productview(request , model_no):

    product= Product.objects.filter(model=model_no)
    return render(request, 'shop/productview.html',{'prods':product[0] })

def category(request , cat):

    criterion1 = Q(product_category__icontains=cat) 
    criterion2 = Q(brand__icontains=cat)
    criterion3 = Q(product_subcategory__icontains=cat)
    criterion4 = Q(model__icontains =cat)
    criterion5 = Q(product_name__icontains =cat) 
    product= Product.objects.filter(criterion1 | criterion2 | criterion3 | criterion4 | criterion5)
        

    if not product:
        return render(request, 'shop/category.html',{'product': product[0:], 'cat':"'Did you mean something else?'" })

    return render(request, 'shop/category.html',{'product': product[0:], 'cat':cat})

def search(request):
    
    srch= request.POST.get('srch', '')
    return category(request,srch)

def checkout(request):
    data = request.POST.get('mycart', 'default')
    y=[]
    if data != 'default' :
        y= json.loads(data)
    mypr=[]
    for i in y:
        mypr.append(i)
    mypr=tuple(mypr)
    productnew=Product.objects.filter(model__in=mypr)
    return render(request, 'shop/checkout.html',{'prods': productnew[0:]})

def order(request):
    if request.method=="POST":
        items= request.POST.get('itemjson', '')
        name=request.POST.get('fn', '')+" "+request.POST.get('ln', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        address=request.POST.get('address1', '')+""+request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('phone', '')
        zip_code=request.POST.get('zip_code', '')
        my_order_id="O"+"-"+str(random.randint(100,10000))+"-"+(datetime.now().strftime("%m%d"))
        order= Order(items=items,name=name,email=email,phone=phone,address=address,city=city,state=state,zip_code=zip_code,my_order_id=my_order_id)
        order.save()
        thank=True
        id=order.my_order_id
        print(items)

    return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})


    

# Create your views here.
