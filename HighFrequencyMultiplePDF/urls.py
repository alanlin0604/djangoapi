from django.urls import path
from . import views

urlpatterns = [
    path("mergePDFs", views.merge_pdfs, name="merge_pdfs"),
]
