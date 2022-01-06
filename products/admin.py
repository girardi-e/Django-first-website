from django.contrib import admin
from .models import Product


# manage Product in the admin area
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


admin.site.register(Product, ProductAdmin)
