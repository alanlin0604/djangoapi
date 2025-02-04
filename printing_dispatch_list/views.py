from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingDispatch
import json

@csrf_exempt
def get_dispatch_list(request):
    """獲取所有印刷派工單"""
    if request.method == "GET":
        records = list(PrintingDispatch.objects.all().values())
        return JsonResponse(records, safe=False, status=200)

@csrf_exempt
def update_nfc(request):
    """更新 NFC 綁定"""
    if request.method == "POST":
        data = json.loads(request.body)
        old_nfc = data.get("old_nfc")
        new_nfc = data.get("new_nfc")

        try:
            dispatch = PrintingDispatch.objects.get(nfc_tag=old_nfc)
            dispatch.nfc_tag = new_nfc
            dispatch.save()
            return JsonResponse({"message": "NFC updated"}, status=200)
        except PrintingDispatch.DoesNotExist:
            return JsonResponse({"error": "Dispatch not found"}, status=404)

@csrf_exempt
def delete_dispatch(request):
    """刪除印刷派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        dispatch_number = data.get("dispatch_number")

        try:
            dispatch = PrintingDispatch.objects.get(dispatch_number=dispatch_number)
            dispatch.delete()
            return JsonResponse({"message": "Printing dispatch deleted"}, status=200)
        except PrintingDispatch.DoesNotExist:
            return JsonResponse({"error": "Printing dispatch not found"}, status=404)
