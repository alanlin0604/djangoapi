from django.urls import path
from . import views

urlpatterns = [
    path("createOrder", views.create_order, name="create_order"),
    path("addOrderPart", views.add_order_part, name="add_order_part"),
    path("updateOrderProgress", views.update_order_progress, name="update_order_progress"),
    path("getOrderDetails", views.get_order_details, name="get_order_details"),
]
