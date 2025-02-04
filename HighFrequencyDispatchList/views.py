from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HighFrequencyDispatchList
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工單列表"""
    if request.method == "GET":
        work_order_number = request.GET.get("workOrderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)

        try:
            data = HighFrequencyDispatchList.objects.filter(work_order_number=work_order_number).values()
            return JsonResponse(list(data), safe=False, status=200)
        except HighFrequencyDispatchList.DoesNotExist:
            return JsonResponse({"error": "No dispatch lists found"}, status=404)

@csrf_exempt
def delete_dispatch(request):
    """刪除派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        dispatch_number = data.get("dispatch_number")
        work_order_number = data.get("work_order_number")
        try:
            HighFrequencyDispatchList.objects.filter(
                work_order_number=work_order_number,
                dispatch_number=dispatch_number,
            ).delete()
            return JsonResponse({"message": "Dispatch deleted"}, status=200)
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
        total_quantity = data.get("total_quantity", 1)  # 避免除以 0

        try:
            dispatch = HighFrequencyDispatchList.objects.get(
                work_order_number=work_order_number,
                dispatch_number=dispatch_number,
            )
            dispatch.completed_quantity = completed_quantity
            dispatch.progress_percentage = (completed_quantity / total_quantity) * 100
            dispatch.save()
            return JsonResponse({"message": "Progress updated"}, status=200)
        except HighFrequencyDispatchList.DoesNotExist:
            return JsonResponse({"error": "Dispatch not found"}, status=404)
