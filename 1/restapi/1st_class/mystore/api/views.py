from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSerializer
from shop.models import Customer

# Create your views here.

# ListApiview
# ListCreateApiView
# RetrieveView
# RetrieveUpdateDeleteApiView

# shop manager


class CustomerApiView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# admin
class CustomerCreateApiView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailsApiView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailsUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
