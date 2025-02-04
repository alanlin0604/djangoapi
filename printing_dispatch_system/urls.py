from django.urls import path
from . import views

urlpatterns = [
    path("directDispatch", views.direct_dispatch, name="direct_dispatch"),
    path("updateProgress", views.update_progress, name="update_progress"),
]
