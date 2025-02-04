from django.urls import path
from . import views

urlpatterns = [
    path("getShoeDetails", views.get_shoe_details, name="get_shoe_details"),
]
