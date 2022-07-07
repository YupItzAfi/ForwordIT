from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.product_list, name="products"),
    path("create-product/", views.create_product, name="create-product"),
    path("product-details/<str:pk>/",
         views.product_details, name="product-details")

]
