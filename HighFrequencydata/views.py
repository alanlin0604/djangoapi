from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HighFrequencyWorkOrder
import json
from datetime import datetime

@csrf_exempt
def get_high_frequency_data(request):
    """獲取高頻派工數據"""
    if request.method == "GET":
        work_order_number = request.GET.get("workorderNumber", "")
        try:
            data = HighFrequencyWorkOrder.objects.filter(work_order_number=work_order_number).values()
            return JsonResponse(list(data), safe=False, status=200)
        except HighFrequencyWorkOrder.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)

@csrf_exempt
def create_high_frequency_work_order(request):
    """新增高頻派工記錄"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            HighFrequencyWorkOrder.objects.create(
                work_order_number=data.get("work_order_number"),
                dispatch_number=data.get("dispatch_number"),
                section=data.get("section"),
                material=data.get("material"),
                size=data.get("size"),
                quantity=data.get("quantity"),
                completed_quantity=data.get("completed_quantity", 0),
                dispatch_time=datetime.now(),
            )
            return JsonResponse({"message": "Work order created"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_high_frequency_work_order(request):
    """更新高頻派工記錄"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            work_order = HighFrequencyWorkOrder.objects.get(
                work_order_number=data.get("work_order_number"),
                dispatch_number=data.get("dispatch_number"),
            )
            work_order.completed_quantity = data.get("completed_quantity", work_order.completed_quantity)
            work_order.dispatch_time = datetime.now()
            work_order.save()
            return JsonResponse({"message": "Work order updated"}, status=200)
        except HighFrequencyWorkOrder.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)

@csrf_exempt
def delete_high_frequency_work_order(request):
    """刪除高頻派工記錄"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            HighFrequencyWorkOrder.objects.filter(
                work_order_number=data.get("work_order_number"),
                dispatch_number=data.get("dispatch_number"),
            ).delete()
            return JsonResponse({"message": "Work order deleted"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
