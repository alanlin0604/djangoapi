from django.urls import path
from . import views

urlpatterns = [
    path("getDispatchList", views.get_dispatch_list, name="get_dispatch_list"),
    path("directDispatch", views.direct_dispatch, name="direct_dispatch"),
    path("updateProgress", views.update_progress, name="update_progress"),
]
