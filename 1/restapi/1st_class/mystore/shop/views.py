from django.shortcuts import redirect, render
from .models import *
from .forms import ProductForm, CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .decotators import unauthenticated_user, allowed_user

# Create your views here.


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "User or Password is either incorrect")
            return render(request, "login.html")
    context = {}
    return render(request, "login.html", context)


def log_out(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {
        "form": form,
    }
    return render(request, "registration.html", context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin', 'customer', 'manager'])
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


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin', 'manager'])
def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "product_list.html", context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
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


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin', 'manager'])
def product_details(request, pk):
    product_details = Product.objects.get(id=pk)

    context = {
        "product_details": product_details,
    }

    return render(request, "product_details.html", context=context)


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin', 'manager'])
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


@login_required(login_url="/login")
@allowed_user(allowed_roles=['admin'])
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
