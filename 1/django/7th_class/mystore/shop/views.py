from django.shortcuts import render
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


def create_product(request):
    form = ProductForm
    products = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "form": form,
        "products": products,
    }

    return render(request, "product_list.html", context=context)


def product_details(request, pk):
    product_details = Product.objects.get(id=pk)
    product = Product.objects.all()

    context = {
        "product_details": product_details,
        "product": product
    }

    return render(request, "product_details.html", context=context)


def about(request):
    return render(request, "about.html")
