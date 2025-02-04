from django.urls import path
from . import views

urlpatterns = [
    path("getAttendanceData", views.get_attendance_data, name="get_attendance_data"),
    path("getProductivityData", views.get_productivity_data, name="get_productivity_data"),
    path("updateProductivity", views.update_productivity_report, name="update_productivity_report"),
]
