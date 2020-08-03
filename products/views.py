from django.shortcuts import render
from .models import Products

def medicine(request):
    medicine = Products.objects
    return render(request, 'products/medicine.html', {'medicine': medicine})

def cart(request):
    medicine = Products.objects
    return render(request, 'products/cart.html', {'medicine': medicine})

