from django.shortcuts import render
from products.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html')


def another(request):
    products = Product.objects.all()
    return render(request, 'home1.html')
