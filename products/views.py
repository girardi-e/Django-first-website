from django.http import HttpResponse
# from django.shortcuts import render


# URL (Uniform Resource Locator -> Address)
# /products -> index
def index(request):
    return HttpResponse("Welcome to PyShop!")


# /products/new
def new(request):
    return HttpResponse("Create new product")
