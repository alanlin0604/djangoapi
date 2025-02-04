from django.urls import path
from . import views

urlpatterns = [
    path("getList", views.get_todo_list, name="get_todo_list"),
    path("addList", views.add_todo_item, name="add_todo_item"),
    path("updateList", views.update_todo_item, name="update_todo_item"),
    path("removeList", views.delete_todo_item, name="delete_todo_item"),
    path("changeStatus", views.change_todo_status, name="change_todo_status"),
]
