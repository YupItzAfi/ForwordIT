from django.contrib import admin

from .models import Category, Product

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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
