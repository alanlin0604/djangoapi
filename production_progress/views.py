from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProductionProgress
import json

@csrf_exempt
def get_progress(request):
    """獲取生產進度"""
    if request.method == "GET":
        work_order_number = request.GET.get("workOrderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)
        data = ProductionProgress.objects.filter(work_order_number=work_order_number).values()
        return JsonResponse(list(data), safe=False, status=200)
