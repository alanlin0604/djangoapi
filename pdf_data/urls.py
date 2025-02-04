from django.urls import path
from . import views

urlpatterns = [
    path("getOrderDetails", views.get_order_details, name="get_order_details"),
    path("getOrderMaterial", views.get_order_material, name="get_order_material"),
    path("getOrderSizes", views.get_order_sizes, name="get_order_sizes"),
]
