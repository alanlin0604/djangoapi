from django.urls import path
from . import views

urlpatterns = [
    path("getPrintingOrder", views.get_printing_order, name="get_printing_order"),
    path("getPrintingMaterial", views.get_printing_material, name="get_printing_material"),
    path("updateNFC", views.update_nfc, name="update_nfc"),
    path("deletePrintingOrder", views.delete_printing_order, name="delete_printing_order"),
]
