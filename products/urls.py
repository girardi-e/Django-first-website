from django.urls import path
from . import views

# /products
urlspatterns = [
    path("", views.index)
]
