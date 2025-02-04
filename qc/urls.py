from django.urls import path
from . import views

urlpatterns = [
    path("getQCData", views.get_qc_data, name="get_qc_data"),
    path("updateQCData", views.update_qc_data, name="update_qc_data"),
]
