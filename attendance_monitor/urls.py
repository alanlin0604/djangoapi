from django.urls import path
from . import views

urlpatterns = [
    path("getAttendanceData", views.get_attendance_data, name="get_attendance_data"),
]
