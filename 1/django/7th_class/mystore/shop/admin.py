from django.contrib import admin
from .models import *

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'date_created']
    list_filter = ['date_created']
    search_fields = ['name', 'phone', 'email']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'date_created']
    list_filter = ['date_created']
    search_fields = ['name']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'product_id', 'status', 'date_created']
    list_filter = ['date_created']
    search_fields = ['customer']


admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
