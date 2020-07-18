from django.shortcuts import render, redirect
from .models import Product, Category, Artisan, Cart
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.contrib import sessions
from django.contrib.auth.decorators import login_required
from search import views as search_views

def home(request):
    if request.GET:
        return search_views.search(request)

    products = {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'handy/home.html', products)

@login_required(login_url='login')
def cart(request):
    y = Cart.objects.filter(use_name=request.user)
    t = 0
    for i in y:
        t+=i.product.price
    items = {
    'items':y,
    'total':t
    }
    products= {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'handy/store.html', items)

@login_required(login_url='login')
def cartview(request,pk):
    x = Product.objects.get(id=pk)
    z = Cart.objects.filter(use_name=request.user, product=x)
    print(len(z))

    if len(z) == 0:
        c = Cart(product=x, use_name=request.user, quantity=1, active = True)
        c.save()
    else:
        z = Cart.objects.get(use_name=request.user, product=x)
        z.quantity = z.quantity+1
        z.save()

    y = Cart.objects.filter(use_name=request.user)
    t = 0
    for i in y:
        t+=((i.product.price)*(i.quantity))
    print(t)
    items = {
    'items':y,
    'total':t
    }
    products= {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }

    return render(request,'handy/store.html',items)

@login_required(login_url='login')
def update_cartview(request):
    print('a')
    data = request.POST
    print(data['quantity'])
    y = Cart.objects.filter(use_name=request.user, product=data['product'])
    y.update(quantity=data['quantity'])
    y = Cart.objects.filter(use_name=request.user, product=data['product'])
    t = 0
    for i in y:
        t+=((i.product.price)*(i.quantity))
    print(t)
    items = {
    'items':y,
    'total':t
    }

    return render(request,'handy/store.html',items)

@login_required(login_url='login')
def del_cartview(request,pk):
    x = Product.objects.get(id=pk)
    z = Cart.objects.filter(use_name=request.user, product=x)
    z.delete()
    y = Cart.objects.filter(use_name=request.user)
    print(y)
    t = 0
    for i in y:
        t+=((i.product.price)*(i.quantity))
    print(t)
    items = {
    'items':y,
    'total':t
    }
    # request.session['del']=1
    return render(request,'handy/store.html',items)

class ProductDetailView(DetailView):
    model = Product

class ArtisanDetailView(DetailView):
    model = Artisan
