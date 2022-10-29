from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('webhooks/stripe/', views.stripe_webhook, name="stripe-webhook"),
    path('create-payment-intent/<int:pk>/<str:currency>',
         views.PaymentIntent.as_view(), name="create-payment-intent"),
    path('registration/', views.registration, name="register"),
    path('add-events/', views.add_events, name="add-events"),
    path('booking/<int:pk>/<str:currency>',
         views.ticket_booking, name="ticket_booking"),
    path('create-checkout-session/<int:pk>/<str:currency>', views.CreateCheckoutSession.as_view(),
         name="create-checkout-session"),
    path('refund/<int:pk>/', views.refund, name="refund"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('create_object/<str:model_name>/',
         views.create_object, name="create-object"),
    path('success/', views.success, name="success"),
    path('cancel/', views.cancel, name="cancel"),

]
