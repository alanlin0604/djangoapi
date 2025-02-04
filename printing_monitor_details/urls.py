from django.urls import path
from . import views

urlpatterns = [
    path("getDailyProduction", views.get_daily_production, name="get_daily_production"),
    path("getSectionProduction", views.get_section_production, name="get_section_production"),
]
