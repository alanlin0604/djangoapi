from django.urls import path
from . import views

urlpatterns = [
    path("getBrands", views.get_brands, name="get_brands"),
]
