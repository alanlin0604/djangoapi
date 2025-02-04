from django.urls import path
from . import views

urlpatterns = [
    path("generatePDF", views.generate_pdf, name="generate_pdf"),
]
