from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Product, Category, Artisan, Cart, ratings
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from search import views as search_views
from django.contrib import sessions
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from orders.models import Orders, Map
from datetime import date, timedelta
from payTm import Checksum

MERCHANT_KEY = 'woRbO8u9VOz6Ti3D'


def home(request):
    if request.GET:
        return search_views.search(request)

    latest = []

    for item in Product.objects.all():
        if ((date.today() -
             item.date_posted.date()) < timedelta(days=10)):
            latest.append(item)

    products = {
        'latest': latest,
        'thumbnails': Product.objects.all(),
        'category0': Category.objects.all()[0],
        'category1': Category.objects.all()[1],
        'category2': Category.objects.all()[2],
        'category3': Category.objects.all()[3],
        'category4': Category.objects.all()[4],
        'artisans': Artisan.objects.all()
    }
    return render(request, 'handy/home.html', products)


@login_required(login_url='login')
def Ordersview(request):

    orders = []

    for order in Orders.objects.all():
        if str(order.user_name) == str(request.user):
            orders.append(order)

    package = {
        'orders': orders,
    }
    return render(request, 'handy/orders.html', package)


@login_required(login_url='login')
def cart(request):
    y = Cart.objects.filter(use_name=request.user)
    t = 0
    for i in y:
        t += i.product.price
    items = {
        'items': y,
        'total': t
    }
    products = {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'handy/store.html', items)


@login_required(login_url='login')
def cartview(request, pk):
    x = Product.objects.get(id=pk)
    z = Cart.objects.filter(use_name=request.user, product=x)
    print(len(z))

    if len(z) == 0:
        c = Cart(product=x, use_name=request.user, quantity=1, active=True)
        c.save()
    else:
        z = Cart.objects.get(use_name=request.user, product=x)
        z.quantity = z.quantity + 1
        z.save()

    y = Cart.objects.filter(use_name=request.user)
    t = 0
    for i in y:
        t += ((i.product.price) * (i.quantity))
    print(t)
    items = {
        'items': y,
        'total': t
    }
    products = {
        'thumbnails': Product.objects.all(),
        'category': Category.objects.all()
    }

    return render(request, 'handy/store.html', items)


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
        t += ((i.product.price) * (i.quantity))
    print(t)
    items = {
        'items': y,
        'total': t
    }

    return render(request, 'handy/store.html', items)


@login_required(login_url='login')
def del_cartview(request, pk):
    x = Product.objects.get(id=pk)
    z = Cart.objects.filter(use_name=request.user, product=x)
    z.delete()
    y = Cart.objects.filter(use_name=request.user)
    print(y)
    t = 0
    for i in y:
        t += ((i.product.price) * (i.quantity))
    print(t)
    items = {
        'items': y,
        'total': t
    }
    # request.session['del']=1
    return render(request, 'handy/store.html', items)


class ProductDetailView(DetailView):
    model = Product


class ArtisanDetailView(DetailView):
    model = Artisan


def update_ratingview(request):
    print(request.user)
    data = request.POST
    print(data)
    try:
        h = ratings.objects.filter(
            user=request.user, product_id=data['product'])
        for i in h:
            x = i.ratings
        h.update(ratings=data['value'])
        y = Product.objects.filter(
            name=data['name'], artisan_id=data['artisan_id'])
        for i in y:
            p = i.no_of_users
            q = i.ratings
        print('a')
        print(x)
        print(p)
        print(q)
        val = float(data['value'])
        temp = (((p * q) - x) + val) / p

        print(temp)
        y.update(ratings=temp)

    except:
        try:
            h = ratings.objects.filter(
                user=request.user, product_id=data['product'])
            for i in h:
                x = i.reviews
            h.update(ratings=data['value'])
            y = Product.objects.filter(
                name=data['name'], artisan_id=data['artisan_id'])
            for i in y:
                p = i.no_of_users
                q = i.ratings
            print('a')
            print(x)
            print(p)
            print(q)
            val = float(data['value'])
            temp = (((p * q) - x) + val) / p

            print(temp)
            y.update(ratings=temp)

        except:
            y = Product.objects.filter(
                name=data['name'], artisan_id=data['artisan_id'])
            for i in y:
                p = i.no_of_users
                q = i.ratings
            val = float(data['value'])
            temp = ((p * q) + val) / (p + 1)
            y.update(ratings=temp, no_of_users=p + 1)
            h = ratings(user=request.user,
                        ratings=data['value'], product_id=data['product'])
            h.save()

    t = data['product']
    return redirect('product-detail', pk=t)


def get_reviewsview(request):
    data = request.GET
    print(data['product'])
    print('abc')
    try:
        print('babai1')
        y = ratings.objects.filter(
            product_id=data['product'], user=request.user)
        for i in y:
            r = i.ratings

        # t = data['product']
        # print(r)
        y = ratings.objects.filter(product_id=data['product'])
        p = []
        q = []
        for i in y:
            p.append(i.reviews)
            q.append(i.user)
        return JsonResponse({"valid": r, "user": q, "reviews": p}, status=200)
    except:
        try:
            print('babai2')
            y = ratings.objects.filter(product_id=data['product'])
            p = []
            q = []
            for i in y:
                p.append(i.reviews)
                q.append(i.user)
            return JsonResponse({"user": q, "reviews": p}, status=200)
        except:
            print('babai3')
            return JsonResponse({"not_there": True}, status=200)


def update_reviewview(request):
    print(request.user)
    data = request.POST
    print(data)
    try:
        h = ratings.objects.filter(
            user=request.user, product_id=data['product'])
        for i in h:
            x = i.reviews
        print(x)
        h.update(reviews=data['value'])
        print('a_undi')
    except:
        print('b')
        try:
            h = ratings.objects.filter(
                user=request.user, product_id=data['product'])
            for i in h:
                x = i.ratings
            print(x)
            h.update(reviews=data['value'])
        except:
            h = ratings(user=request.user,
                        reviews=data['value'], product_id=data['product'])
            h.save()
    t = data['product']
    return redirect('product-detail', pk=t)


def Checkout(request):
    global s
    y = Cart.objects.filter(use_name=request.user)
    print(y)
    t = 0
    for i in y:
        t += (i.product.price * i.quantity)
    items = {
        'items': y,
        'total': t
    }
    if request.method == "POST":
        # items_json = JSONField()
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        count = 0
        for item in y:
            count = count + 1
            z = Product.objects.filter(name=item.product.name, artisan_id=item.product.artisan_id,
                                       category=item.product.category)
            print(z)
            order = Orders(name=name, user_name=request.user.username, email=email,
                           address=str(address1) + " " + str(address2),
                           city=city, state=state,
                           zip_code=zip_code, phone=phone, product=z[0], quantity=item.quantity,
                           net_price=z[0].price * item.quantity)
            order.save()
            if count == 1:
                x = order.order_id
        m = Map(user_name=request.user, start=x, count=count, amount=t)
        m.save()
        param_dict = {
            'MID': 'MQUWBT37855796215302',
            'ORDER_ID': str(m.ord_id),
            'TXN_AMOUNT': str(t),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://localhost:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(
            param_dict, MERCHANT_KEY)
        return render(request, 'handy/paytm.html', {'param_dict': param_dict})
        # return redirect(reverse('payment_process'))
    return render(request, 'handy/checkout.html', items)


class ProductDetailView(DetailView):
    model = Product


class ArtisanDetailView(DetailView):
    model = Artisan


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            y = Cart.objects.filter(use_name=request.user)
            y.delete()
            print(y)
            print('order successful')
        else:
            print('order was not successful because ' +
                  response_dict['RESPMSG'])
    return render(request, 'handy/paymentstatus.html', {'response': response_dict})
