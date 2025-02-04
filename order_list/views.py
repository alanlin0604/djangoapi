from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderPart
import json

@csrf_exempt
def get_orders(request):
    """獲取所有製令單"""
    if request.method == "GET":
        orders = list(Order.objects.all().values())
        return JsonResponse(orders, safe=False, status=200)

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
                "last_updated": order.last_updated,
                "progress_percentage": order.progress_percentage,
                "parts": parts
            }, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

@csrf_exempt
def delete_order(request):
    """刪除指定製令單"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")

        try:
            order = Order.objects.get(order_number=order_number)
            order.delete()
            return JsonResponse({"message": "Order deleted"}, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
