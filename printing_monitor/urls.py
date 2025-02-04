from django.urls import path
from . import views

urlpatterns = [
    path("getOverview", views.get_printing_overview, name="get_printing_overview"),
    path("updateProgress", views.update_printing_progress, name="update_printing_progress"),
]
