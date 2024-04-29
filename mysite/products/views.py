from django.http import HttpResponse
from django.shortcuts import render
from . import forms


# Create your views here.
def add_product(request):
    if request.method == "GET":
        form = forms.ProductForm(request.GET)
        if form.is_valid():
            form.save()
            return HttpResponse('add successful')
    else:
        form = forms.ProductForm()
    return render(request, 'forms.html', {
        "form": form,
    })
