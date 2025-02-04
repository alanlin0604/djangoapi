from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchOrder
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工單列表"""
    if request.method == "GET":
        orders = DispatchOrder.objects.all().values()
        data = list(orders)
        return JsonResponse(data, safe=False, status=200)

@csrf_exempt
def create_dispatch_order(request):
    """新增派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        model_number = data.get('model_number')
        progress = data.get('progress', 0.0)
        try:
            DispatchOrder.objects.create(
                work_order_number=work_order_number,
                model_number=model_number,
                progress=progress,
            )
            return JsonResponse({'message': 'Dispatch order created'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def delete_dispatch_order(request):
    """刪除派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        try:
            order = DispatchOrder.objects.get(work_order_number=work_order_number)
            order.delete()
            return JsonResponse({'message': 'Dispatch order deleted'}, status=200)
        except DispatchOrder.DoesNotExist:
            return JsonResponse({'error': 'Dispatch order not found'}, status=404)
