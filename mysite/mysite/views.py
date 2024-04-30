from django.shortcuts import render
from products.models import Product
from donors.models import Donor


def home(request):
    products = Product.objects.all()
    donors = Donor.objects.all()
    return render(request, 'home.html', {
        "products": products,
        "donors": donors,
    })


def another(request):
    products = Product.objects.all()
    return render(request, 'home1.html')
