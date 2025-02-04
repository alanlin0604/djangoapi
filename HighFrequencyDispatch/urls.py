from django.urls import path
from . import views

urlpatterns = [
    path("getDispatchList", views.get_dispatch_list, name="get_dispatch_list"),
    path("updateProgress", views.update_dispatch_progress, name="update_dispatch_progress"),
    path("updateSection", views.update_section, name="update_section"),
]
