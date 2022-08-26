from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerApiView.as_view()),
    path('create-customers/', views.CustomerCreateApiView.as_view()),
    path('customer/<str:pk>', views.CustomerDetailsApiView.as_view()),
    path('update-customer/<str:pk>', views.CustomerDetailsUpdateApiView.as_view()),
]
