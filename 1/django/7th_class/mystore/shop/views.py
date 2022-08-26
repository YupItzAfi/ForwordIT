from django.shortcuts import redirect, render
from .models import *
from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_products = len(products)
    total_customers = len(customers)
    total_orders = len(orders)

    context = {
        "products": products,
        "total_customers": total_customers,
        "total_orders": total_orders,
        "total_products": total_products
    }

    return render(request, "index.html", context=context)


def product_list(request):
    return render(request, "product_list.html")


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "product_list.html", context=context)


def create_product(request):
    form = ProductForm

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }

    return render(request, "product_create.html", context=context)


def product_details(request, pk):
    product_details = Product.objects.get(id=pk)

    context = {
        "product_details": product_details,
    }

    return render(request, "product_details.html", context=context)


def product_update(request, pk):
    product_update = Product.objects.get(id=pk)
    form = ProductForm(instance=product_update)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product_update)
        if form.is_valid():
            form.save()
            return redirect('product-list')

    context = {
        "form": form,
    }
    return render(request, "product_create.html", context=context)


def product_delete(request, pk):
    product_delete = Product.objects.get(id=pk)

    if request.method == 'POST':
        product_delete.delete()
        return redirect('product-list')

    context = {
        "product_item": product_delete,
    }

    return render(request, "product_list.html", context=context)


def about(request):
    return render(request, "about.html")
