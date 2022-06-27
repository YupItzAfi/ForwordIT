from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    customers = Customer
    order = Order
    # cus_orders = order.customer_id.name
    cus_orders = order.customer_id.field.model.objects.all()

    info = {
        "customers": customers.objects.all(),
        "cus_orders": cus_orders,
    }
    return render(request, "index.html", context=info)


def about(request):
    return render(request, "about.html")
