from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.table_page, name='table_page'),
    path('get_table/', views.get_table, name='get_table'),
    path('update_table/', views.update_table, name='update_table'),
]
