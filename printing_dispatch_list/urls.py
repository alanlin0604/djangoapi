from django.urls import path
from . import views

urlpatterns = [
    path("getDispatchList", views.get_dispatch_list, name="get_dispatch_list"),
    path("updateNFC", views.update_nfc, name="update_nfc"),
    path("deleteDispatch", views.delete_dispatch, name="delete_dispatch"),
]
