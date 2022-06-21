from django.contrib import admin
from .models import *

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description', 'image']
    list_filter = ['category_name']
    search_fields = ['category_name']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'slug',
                    'category_id', 'price', 'is_active']
    list_filter = ['price', 'is_active']
    search_fields = ['product_name', 'slug']
    prepopulated_fields = {'slug': ['product_name', ]}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'product_id', 'status', 'date_created']
    list_filter = ['date_created', 'product_id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)
