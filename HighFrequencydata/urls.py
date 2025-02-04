from django.urls import path
from . import views

urlpatterns = [
    path("getData", views.get_high_frequency_data, name="get_high_frequency_data"),
    path("createWorkOrder", views.create_high_frequency_work_order, name="create_high_frequency_work_order"),
    path("updateWorkOrder", views.update_high_frequency_work_order, name="update_high_frequency_work_order"),
    path("deleteWorkOrder", views.delete_high_frequency_work_order, name="delete_high_frequency_work_order"),
]
