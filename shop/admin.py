from django.contrib import admin

from .models import Product,Order
@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ("my_order_id", "name")
    search_fields = ("my_order_id", "name")


@admin.register(Product)



class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_name", "model")
    search_fields = ("model", "product_category" )
    