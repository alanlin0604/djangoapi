from django.urls import path
from . import views

urlpatterns = [
    path("getProgress", views.get_progress, name="get_progress"),
]
