from django.urls import path
from . import views

urlpatterns = [
    path("getOrders", views.get_orders, name="get_orders"),
]
