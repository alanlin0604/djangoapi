from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingProduction
import json

@csrf_exempt
def get_daily_production(request):
    """獲取單日的生產進度"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")
        if not order_number:
            return JsonResponse({"error": "Missing order number"}, status=400)

        records = list(PrintingProduction.objects.filter(order__order_number=order_number).values("date", "total_quantity", "completed_quantity", "progress_percentage"))
        return JsonResponse(records, safe=False, status=200)

@csrf_exempt
def get_section_production(request):
    """獲取特定部位的生產進度"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")
        section = request.GET.get("section", "")

        if not order_number or not section:
            return JsonResponse({"error": "Missing parameters"}, status=400)

        records = list(PrintingProduction.objects.filter(order__order_number=order_number, section=section).values("date", "total_quantity", "completed_quantity", "progress_percentage"))
        return JsonResponse(records, safe=False, status=200)
