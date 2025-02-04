from django.urls import path
from . import views

urlpatterns = [
    path('getWorkOrderData', views.get_work_order_data, name='get_work_order_data'),
    path('updateWorkOrderProgress', views.update_work_order_progress, name='update_work_order_progress'),
    path('bindNFC', views.bind_nfc, name='bind_nfc'),
]
