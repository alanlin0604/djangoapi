from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ToDoItem
import json

@csrf_exempt
def get_todo_list(request):
    """獲取所有待辦事項"""
    if request.method == "GET":
        todos = list(ToDoItem.objects.all().values())
        return JsonResponse(todos, safe=False, status=200)

@csrf_exempt
def add_todo_item(request):
    """新增待辦事項"""
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            return JsonResponse({"error": "Title and content are required"}, status=400)

        todo = ToDoItem.objects.create(title=title, content=content)
        return JsonResponse({"message": "To-Do item added", "id": todo.id}, status=201)

@csrf_exempt
def update_todo_item(request):
    """更新待辦事項"""
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")
        title = data.get("title")
        content = data.get("content")

        try:
            todo = ToDoItem.objects.get(id=item_id)
            todo.title = title
            todo.content = content
            todo.save()
            return JsonResponse({"message": "To-Do item updated"}, status=200)
        except ToDoItem.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)

@csrf_exempt
def delete_todo_item(request):
    """刪除待辦事項"""
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")

        try:
            todo = ToDoItem.objects.get(id=item_id)
            todo.delete()
            return JsonResponse({"message": "To-Do item deleted"}, status=200)
        except ToDoItem.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)

@csrf_exempt
def change_todo_status(request):
    """變更待辦事項狀態"""
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("id")
        status = data.get("status")

        try:
            todo = ToDoItem.objects.get(id=item_id)
            todo.status = status
            todo.save()
            return JsonResponse({"message": "Status updated"}, status=200)
        except ToDoItem.DoesNotExist:
            return JsonResponse({"error": "Item not found"}, status=404)
