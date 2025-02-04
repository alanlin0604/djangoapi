from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HighFrequencyDispatch
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工列表"""
    if request.method == "GET":
        work_order_number = request.GET.get("workOrderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)
        data = HighFrequencyDispatch.objects.filter(work_order_number=work_order_number).values()
        return JsonResponse(list(data), safe=False, status=200)

@csrf_exempt
def direct_dispatch(request):
    """直接派工"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        section = data.get("section")
        size = data.get("size")
        quantity = data.get("quantity", 0)
        dispatch_number = data.get("dispatch_number", "")

        try:
            HighFrequencyDispatch.objects.create(
                work_order_number=work_order_number,
                dispatch_number=dispatch_number,
                section=section,
                size=size,
                quantity=quantity,
                completed_quantity=0,
                progress_percentage=0.0,
            )
            return JsonResponse({"message": "Dispatch created"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_progress(request):
    """更新派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        dispatch_number = data.get("dispatch_number")
        completed_quantity = data.get("completed_quantity", 0)
        total_quantity = data.get("quantity", 1)

        try:
            dispatch = HighFrequencyDispatch.objects.get(
                work_order_number=work_order_number,
                dispatch_number=dispatch_number
            )
            dispatch.completed_quantity = completed_quantity
            dispatch.progress_percentage = (completed_quantity / total_quantity) * 100
            dispatch.save()
            return JsonResponse({"message": "Progress updated"}, status=200)
        except HighFrequencyDispatch.DoesNotExist:
            return JsonResponse({"error": "Dispatch not found"}, status=404)
