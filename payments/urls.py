from django.urls import path
from . import views

urlpatterns = [
    path('', views.donation, name=''),
    path('payment_success', views.successful_payment, name='payment_success'),
    path('payment_failed', views.failed_payment, name='payment_failed'),
]