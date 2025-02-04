from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import HighFrequencyMonitor
import json
from datetime import datetime

@csrf_exempt
def get_monitor_list(request):
    """獲取監控列表"""
    if request.method == "GET":
        work_order_number = request.GET.get("workOrderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)
        data = HighFrequencyMonitor.objects.filter(work_order_number=work_order_number).values()
        return JsonResponse(list(data), safe=False, status=200)

@csrf_exempt
def update_progress(request):
    """更新監控進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        section = data.get("section")
        completed_quantity = data.get("completed_quantity", 0)
        total_quantity = data.get("quantity", 1)

        try:
            monitor = HighFrequencyMonitor.objects.get(
                work_order_number=work_order_number,
                section=section
            )
            monitor.completed_quantity = completed_quantity
            monitor.progress_percentage = (completed_quantity / total_quantity) * 100
            monitor.save()
            return JsonResponse({"message": "Progress updated"}, status=200)
        except HighFrequencyMonitor.DoesNotExist:
            return JsonResponse({"error": "Monitor data not found"}, status=404)

@csrf_exempt
def get_progress_chart(request):
    """返回進度圖表數據"""
    if request.method == "GET":
        work_order_number = request.GET.get("workOrderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)

        try:
            data = HighFrequencyMonitor.objects.filter(work_order_number=work_order_number).values(
                "section", "progress_percentage"
            )
            labels = [item["section"] for item in data]
            progress_values = [item["progress_percentage"] for item in data]

            return JsonResponse({
                "labels": labels,
                "data": progress_values
            }, status=200)
        except HighFrequencyMonitor.DoesNotExist:
            return JsonResponse({"error": "No progress data found"}, status=404)
