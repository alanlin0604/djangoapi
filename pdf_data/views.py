from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, OrderPart
import json

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
                "color": order.color,
                "sole": order.sole,
                "last": order.last,
                "logo": order.logo,
                "parts": parts
            }, status=200)
        except Order.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

@csrf_exempt
def get_order_material(request):
    """獲取製令單材料資訊"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")
        part_name = request.GET.get("section", "")

        if not order_number or not part_name:
            return JsonResponse({"error": "Missing parameters"}, status=400)

        try:
            part = OrderPart.objects.get(order__order_number=order_number, part_name=part_name)
            return JsonResponse({
                "part_name": part.part_name,
                "material": part.material
            }, status=200)
        except OrderPart.DoesNotExist:
            return JsonResponse({"error": "Material not found"}, status=404)

@csrf_exempt
def get_order_sizes(request):
    """獲取製令單尺寸數量資訊"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")

        if not order_number:
            return JsonResponse({"error": "Missing order number"}, status=400)

        try:
            parts = list(OrderPart.objects.filter(order__order_number=order_number).values("size", "quantity"))
            total_quantity = sum(part["quantity"] for part in parts)
            return JsonResponse({
                "sizes": parts,
                "total_quantity": total_quantity
            }, status=200)
        except OrderPart.DoesNotExist:
            return JsonResponse({"error": "Sizes not found"}, status=404)
