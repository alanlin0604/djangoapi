from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WorkOrder, NFC
import json

@csrf_exempt
def get_work_order_data(request):
    """獲取工作單資料"""
    if request.method == "GET":
        work_order_number = request.GET.get('number', '')
        if work_order_number:
            try:
                work_order = WorkOrder.objects.get(work_order_number=work_order_number)
                data = {
                    'work_order_number': work_order.work_order_number,
                    'part': work_order.part,
                    'material': work_order.material,
                    'size': work_order.size,
                    'quantity': work_order.quantity,
                    'progress': work_order.progress,
                }
                return JsonResponse(data, status=200)
            except WorkOrder.DoesNotExist:
                return JsonResponse({'error': 'Work order not found'}, status=404)
        return JsonResponse({'error': 'Missing work order number'}, status=400)

@csrf_exempt
def update_work_order_progress(request):
    """更新工作單進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        progress = data.get('progress')
        try:
            work_order = WorkOrder.objects.get(work_order_number=work_order_number)
            work_order.progress = progress
            work_order.save()
            return JsonResponse({'message': 'Progress updated'}, status=200)
        except WorkOrder.DoesNotExist:
            return JsonResponse({'error': 'Work order not found'}, status=404)

@csrf_exempt
def bind_nfc(request):
    """綁定 NFC 標籤"""
    if request.method == "POST":
        data = json.loads(request.body)
        new_nfc = data.get('new')
        old_nfc = data.get('old')
        try:
            nfc = NFC.objects.get(nfc_id=old_nfc)
            nfc.nfc_id = new_nfc
            nfc.save()
            return JsonResponse({'message': 'NFC updated'}, status=200)
        except NFC.DoesNotExist:
            return JsonResponse({'error': 'NFC not found'}, status=404)
