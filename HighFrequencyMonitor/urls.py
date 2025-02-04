from django.urls import path
from . import views

urlpatterns = [
    path("getMonitorList", views.get_monitor_list, name="get_monitor_list"),
    path("updateProgress", views.update_progress, name="update_progress"),
    path("getProgressChart", views.get_progress_chart, name="get_progress_chart"),
]
