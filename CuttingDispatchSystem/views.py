from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PartDispatch
import json
from datetime import datetime

@csrf_exempt
def get_dispatch_list(request):
    """獲取派工列表"""
    if request.method == "GET":
        work_order_number = request.GET.get('workorderNumber', '')
        if work_order_number:
            data = PartDispatch.objects.filter(work_order_number=work_order_number).values()
        else:
            data = PartDispatch.objects.all().values()
        return JsonResponse(list(data), safe=False, status=200)

@csrf_exempt
def update_dispatch_progress(request):
    """更新派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get('work_order_number')
        part_name = data.get('part_name')
        progress = data.get('progress', 0)
        try:
            dispatch = PartDispatch.objects.get(work_order_number=work_order_number, part_name=part_name)
            dispatch.dispatch_progress = progress
            dispatch.save()
            return JsonResponse({'message': 'Progress updated'}, status=200)
        except PartDispatch.DoesNotExist:
            return JsonResponse({'error': 'Dispatch not found'}, status=404)

@csrf_exempt
def create_dispatch_record(request):
    """新增派工記錄"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            PartDispatch.objects.create(
                work_order_number=data.get('work_order_number'),
                part_name=data.get('part_name'),
                material=data.get('material'),
                size=data.get('size'),
                quantity=data.get('quantity'),
                unit=data.get('unit'),
                dispatch_progress=data.get('dispatch_progress', 0),
            )
            return JsonResponse({'message': 'Dispatch record created'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def batch_update_dispatch_progress(request):
    """批量更新派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        updates = data.get('updates', [])
        for update in updates:
            work_order_number = update.get('work_order_number')
            part_name = update.get('part_name')
            progress = update.get('progress', 0)
            try:
                dispatch = PartDispatch.objects.get(work_order_number=work_order_number, part_name=part_name)
                dispatch.dispatch_progress = progress
                dispatch.save()
            except PartDispatch.DoesNotExist:
                continue
        return JsonResponse({'message': 'Batch progress updated'}, status=200)
