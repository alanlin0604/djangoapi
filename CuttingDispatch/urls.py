from django.urls import path
from . import views

urlpatterns = [
    path('getList', views.get_dispatch_list, name='get_dispatch_list'),
    path('createOrder', views.create_dispatch_order, name='create_dispatch_order'),
    path('deleteOrder', views.delete_dispatch_order, name='delete_dispatch_order'),
]
