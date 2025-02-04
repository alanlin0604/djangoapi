from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderPart
import json

@csrf_exempt
def create_order(request):
    """新增製令單"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")
        model_number = data.get("model_number")
        total_quantity = data.get("total_quantity", 0)

        if Order.objects.filter(order_number=order_number).exists():
            return JsonResponse({"error": "Order already exists"}, status=400)

        order = Order.objects.create(
            order_number=order_number,
            model_number=model_number,
            total_quantity=total_quantity,
            completed_quantity=0,
            progress_percentage=0.0
        )

        return JsonResponse({"message": "Order created", "order_number": order.order_number}, status=201)

@csrf_exempt
def add_order_part(request):
    """新增製令單部位"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")
        part_name = data.get("part_name")
        material = data.get("material")
        size = data.get("size")
        quantity = data.get("quantity", 0)

        try:
            order = Order.objects.get(order_number=order_number)
            OrderPart.objects.create(
                order=order,
                part_name=part_name,
                material=material,
                size=size,
                quantity=quantity,
                completed_quantity=0
            )
            return JsonResponse({"message": "Part added"}, status=201)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

@csrf_exempt
def update_order_progress(request):
    """更新製令單進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")

        try:
            order = Order.objects.get(order_number=order_number)
            parts = OrderPart.objects.filter(order=order)
            total_quantity = sum(part.quantity for part in parts)
            completed_quantity = sum(part.completed_quantity for part in parts)
            progress_percentage = (completed_quantity / total_quantity) * 100 if total_quantity > 0 else 0

            order.total_quantity = total_quantity
            order.completed_quantity = completed_quantity
            order.progress_percentage = progress_percentage
            order.save()

            return JsonResponse({"message": "Progress updated", "progress": progress_percentage}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

@csrf_exempt
def get_order_details(request):
    """獲取製令單詳細資訊"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")
        if not order_number:
            return JsonResponse({"error": "Missing order number"}, status=400)

        try:
            order = Order.objects.get(order_number=order_number)
            parts = list(OrderPart.objects.filter(order=order).values())
            return JsonResponse({
                "order_number": order.order_number,
                "model_number": order.model_number,
                "total_quantity": order.total_quantity,
                "completed_quantity": order.completed_quantity,
                "progress_percentage": order.progress_percentage,
                "parts": parts
            }, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
