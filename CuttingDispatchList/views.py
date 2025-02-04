from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import DispatchList
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工單列表"""
    if request.method == "GET":
        work_order_number = request.GET.get('workorderNumber', '')
        if work_order_number:
            data = DispatchList.objects.filter(work_order_number=work_order_number).values()
        else:
            data = DispatchList.objects.all().values()
        return JsonResponse(list(data), safe=False, status=200)

@csrf_exempt
def update_print_status(request):
    """更新列印狀態"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        dispatch_time = data.get('dispatch_time')
        print_status = data.get('print_status', '列印完成')
        try:
            dispatch = DispatchList.objects.get(work_order_number=work_order_number, dispatch_time=dispatch_time)
            dispatch.print_status = print_status
            dispatch.save()
            return JsonResponse({'message': 'Print status updated'}, status=200)
        except DispatchList.DoesNotExist:
            return JsonResponse({'error': 'Dispatch not found'}, status=404)

@csrf_exempt
def delete_dispatch(request):
    """刪除派工單"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        dispatch_time = data.get('dispatch_time')
        try:
            dispatch = DispatchList.objects.get(work_order_number=work_order_number, dispatch_time=dispatch_time)
            dispatch.delete()
            return JsonResponse({'message': 'Dispatch deleted'}, status=200)
        except DispatchList.DoesNotExist:
            return JsonResponse({'error': 'Dispatch not found'}, status=404)
