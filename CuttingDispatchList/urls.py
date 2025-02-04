from django.urls import path
from . import views

urlpatterns = [
    path('getDispatchList', views.get_dispatch_list, name='get_dispatch_list'),
    path('updatePrintStatus', views.update_print_status, name='update_print_status'),
    path('deleteDispatch', views.delete_dispatch, name='delete_dispatch'),
]
