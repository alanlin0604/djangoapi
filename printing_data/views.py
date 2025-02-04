from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingOrder, PrintingMaterial
import json

@csrf_exempt
def get_printing_order(request):
    """獲取印刷派工單"""
    if request.method == "GET":
        work_order_number = request.GET.get("work_order_number", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)

        records = list(PrintingOrder.objects.filter(work_order_number=work_order_number).values())
        return JsonResponse(records, safe=False, status=200)

@csrf_exempt
def get_printing_material(request):
    """獲取印刷材料資訊"""
    if request.method == "GET":
        work_order_number = request.GET.get("work_order_number", "")
        part_name = request.GET.get("section", "")

        if not work_order_number or not part_name:
            return JsonResponse({"error": "Missing parameters"}, status=400)

        try:
            material = PrintingMaterial.objects.get(work_order_number__work_order_number=work_order_number, part_name=part_name)
            return JsonResponse({
                "part_name": material.part_name,
                "material_name": material.material_name
            }, status=200)
        except PrintingMaterial.DoesNotExist:
            return JsonResponse({"error": "Material not found"}, status=404)

@csrf_exempt
def update_nfc(request):
    """更新 NFC 綁定"""
    if request.method == "POST":
        data = json.loads(request.body)
        old_nfc = data.get("old_nfc")
        new_nfc = data.get("new_nfc")

        try:
            order = PrintingOrder.objects.get(nfc_tag=old_nfc)
            order.nfc_tag = new_nfc
            order.save()
            return JsonResponse({"message": "NFC updated"}, status=200)
        except PrintingOrder.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)

@csrf_exempt
def delete_printing_order(request):
    """刪除印刷派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        dispatch_number = data.get("dispatch_number")

        try:
            order = PrintingOrder.objects.get(dispatch_number=dispatch_number)
            order.delete()
            return JsonResponse({"message": "Printing order deleted"}, status=200)
        except PrintingOrder.DoesNotExist:
            return JsonResponse({"error": "Printing order not found"}, status=404)
