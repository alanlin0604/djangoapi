from django.urls import path
from . import views

urlpatterns = [
    path("mergePrintingPDFs", views.merge_printing_pdfs, name="merge_printing_pdfs"),
]
