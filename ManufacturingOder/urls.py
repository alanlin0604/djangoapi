from django.urls import path
from . import views

urlpatterns = [
    path('MO.html', views.mo_view, name='mo_view'),
    path('data/', views.display_data, name='display_data'),
    path('remove/<str:order_id>/', views.remove_item, name='remove_item'),
    path('refresh/', views.refresh_data, name='refresh_data'),
]