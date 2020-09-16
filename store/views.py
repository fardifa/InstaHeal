from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .utils import cookieCart, cartData, guestOrder
from django.db import connection
from django.db.models import Q
from django.shortcuts import render,get_object_or_404



def home(request):
	return render(request,'store/home.html')

def success(request):
	return render(request,'store/success.html')

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def search(request):
	query = None
	results = []
	if request.method == "GET" :
		query = request.GET.get("search")
		results = Product.objects.filter(Q(name__icontains = query))
		#with connection.cursor() as cursor:
		#	cursor.execute("Select * from store_product where store_product.name = %s", [query])
		#results = Product.objects.raw("Select * from store_product where store_product.name = %s", [query])
	return render(request, 'store/search.html', {'query' : query , 'results':results})

def allblogs(request):
    bloglists = Bloglist.objects
    return render(request,'store/allblogs.html',{'bloglists':bloglists})

def detail(request,blog_id):
    detailblog = get_object_or_404(Bloglist,pk=blog_id)
    return render(request,'store/detail.html',{'blog':detailblog})

def specialist(request):
    specialist = Specialist.objects
    return render(request,'store/specialist.html',{'specialist':specialist})
