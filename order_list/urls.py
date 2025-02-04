from django.urls import path
from . import views

urlpatterns = [
    path("getOrders", views.get_orders, name="get_orders"),
    path("getOrderDetails", views.get_order_details, name="get_order_details"),
    path("deleteOrder", views.delete_order, name="delete_order"),
]
