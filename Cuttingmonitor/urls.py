from django.urls import path
from . import views

urlpatterns = [
    path("getWorkOrderProgress", views.get_work_order_progress, name="get_work_order_progress"),
    path("updateCompletedQuantity", views.update_completed_quantity, name="update_completed_quantity"),
    path("getPartProgress", views.get_part_progress, name="get_part_progress"),
    path("createWorkOrder", views.create_work_order, name="create_work_order"),
]
