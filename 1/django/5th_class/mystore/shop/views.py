from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    customers = Customer.objects.all()
    order = Order
    cus_orders = order.customer_id.field.name

    info = {
        "name": "An Nafie",
        "address": "1001@1001",
        "phone": "69636232",
        "customers": customers,
        "cus_orders": cus_orders,
    }
    return render(request, "index.html", context=info)


def about(request):
    return render(request, "about.html")
