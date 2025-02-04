from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingOrder
import json

@csrf_exempt
def get_printing_overview(request):
    """獲取所有製令單的印刷進度總覽"""
    if request.method == "GET":
        orders = list(PrintingOrder.objects.all().values())
        return JsonResponse(orders, safe=False, status=200)

@csrf_exempt
def update_printing_progress(request):
    """更新印刷派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")
        progress = data.get("progress")

        try:
            order = PrintingOrder.objects.get(order_number=order_number)
            order.progress_percentage = progress
            order.save()
            return JsonResponse({"message": "Progress updated"}, status=200)
        except PrintingOrder.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
