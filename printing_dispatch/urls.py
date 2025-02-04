from django.urls import path
from . import views

urlpatterns = [
    path("getPrintingDispatch", views.get_printing_dispatch, name="get_printing_dispatch"),
    path("updatePrintingSection", views.update_printing_section, name="update_printing_section"),
    path("updatePrintingProgress", views.update_printing_progress, name="update_printing_progress"),
    path("deletePrintingDispatch", views.delete_printing_dispatch, name="delete_printing_dispatch"),
]
