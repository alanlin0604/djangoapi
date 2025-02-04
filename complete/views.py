from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import WorkOrder

def get_table(request):
    workorder_number = request.GET.get('workorderNumber', '')
    work_orders = WorkOrder.objects.filter(workorder_number=workorder_number)

    # 將數據轉換為 JSON 格式返回
    data = [
        {
            'workorder_number': wo.workorder_number,
            'part': wo.part,
            'size': wo.size,
            'quantity': wo.quantity,
            'completed_quantity': wo.completed_quantity,
            'incomplete_quantity': wo.incomplete_quantity,
            'progress': float(wo.progress),
        }
        for wo in work_orders
    ]
    return JsonResponse(data, safe=False)

def update_table(request):
    if request.method == 'POST':
        workorder_number = request.POST.get('workorder_number')
        part = request.POST.get('part')
        size = request.POST.get('size')
        completed_quantity = int(request.POST.get('completed_quantity'))

        work_order = get_object_or_404(
            WorkOrder, 
            workorder_number=workorder_number, 
            part=part, 
            size=size
        )
        work_order.completed_quantity = completed_quantity
        work_order.progress = (completed_quantity / work_order.quantity) * 100
        work_order.save()

        return JsonResponse({'status': 'success', 'message': '更新成功！'})
    return JsonResponse({'status': 'error', 'message': '無效的請求方式'}, status=400)

def table_page(request):
    return render(request, 'api.html')
