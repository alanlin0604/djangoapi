from django.urls import path
from . import views

urlpatterns = [
    path("members", views.check_existing_users, name="check_existing_users"),
    path("register", views.register_user, name="register_user"),
]
