from django.urls import path
from . import views

urlpatterns = [
    path("addShoe", views.add_shoe, name="add_shoe"),
]
