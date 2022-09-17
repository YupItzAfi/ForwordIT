from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('registration/', views.registration, name="register"),
    path('add-events/', views.add_events, name="add-events"),
    path('booking/', views.ticket_booking, name="ticket_booking"),
]
