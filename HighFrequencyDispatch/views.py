from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HighFrequencyDispatch
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工列表"""
    if request.method == "GET":
        try:
            data = HighFrequencyDispatch.objects.values(
                "work_order_number", "progress_percentage", "section", "material", "dispatch_time"
            )
            return JsonResponse(list(data), safe=False, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

@csrf_exempt
def update_dispatch_progress(request):
    """更新派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        progress = data.get("progress", 0)
        try:
            dispatch = HighFrequencyDispatch.objects.get(work_order_number=work_order_number)
            dispatch.progress_percentage = progress
            dispatch.save()
            return JsonResponse({"message": "Progress updated", "progress": progress}, status=200)
        except HighFrequencyDispatch.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)

@csrf_exempt
def update_section(request):
    """更新部位信息"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        section = data.get("section")
        try:
            dispatch = HighFrequencyDispatch.objects.get(work_order_number=work_order_number)
            dispatch.section = section
            dispatch.save()
            return JsonResponse({"message": "Section updated", "section": section}, status=200)
        except HighFrequencyDispatch.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)
