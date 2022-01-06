from django.http import HttpResponse
from .models import Product
from django.shortcuts import render


# URL (Uniform Resource Locator -> Address)
# /products -> index
def index(request):
    products = Product.objects.all()
    return render(request, "index.html")


# /products/new
def new(request):
    return HttpResponse("New products")
