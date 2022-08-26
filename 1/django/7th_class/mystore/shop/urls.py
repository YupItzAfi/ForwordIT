from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("create-product/", views.create_product, name="create-product"),
    path("product-list/", views.product_list, name="product-list"),
    path("product-details/<str:pk>/",
         views.product_details, name="product-details"),
    path("product-update/<str:pk>/", views.product_update, name="product-update"),
    path("product-delete/<str:pk>/", views.product_delete, name="product-delete"),

]
