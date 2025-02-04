from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import QualityControl
import json

@csrf_exempt
def get_qc_data(request):
    """獲取製令單 QC 數據"""
    if request.method == "GET":
        order_number = request.GET.get("order_number", "")
        process_type = request.GET.get("process_type", "")

        if not order_number or not process_type:
            return JsonResponse({"error": "Missing parameters"}, status=400)

        records = list(QualityControl.objects.filter(order_number=order_number, process_type=process_type).values())
        return JsonResponse(records, safe=False, status=200)

@csrf_exempt
def update_qc_data(request):
    """更新 QC 數據"""
    if request.method == "POST":
        data = json.loads(request.body)
        order_number = data.get("order_number")
        section = data.get("section")
        process_type = data.get("process_type")
        defect_count = data.get("defect_count", 0)
        defect_rate = data.get("defect_rate", 0.0)

        try:
            qc_record, created = QualityControl.objects.update_or_create(
                order_number=order_number, section=section, process_type=process_type,
                defaults={"defect_count": defect_count, "defect_rate": defect_rate}
            )
            return JsonResponse({"message": "QC data updated"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
