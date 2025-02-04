from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingDispatch
import json

@csrf_exempt
def get_printing_dispatch(request):
    """獲取所有印刷派工單"""
    if request.method == "GET":
        records = list(PrintingDispatch.objects.all().values())
        return JsonResponse(records, safe=False, status=200)

@csrf_exempt
def update_printing_section(request):
    """更新印刷派工的部位"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        new_section = data.get("section")

        try:
            dispatch = PrintingDispatch.objects.get(work_order_number=work_order_number)
            dispatch.section = new_section
            dispatch.save()
            return JsonResponse({"message": "Section updated"}, status=200)
        except PrintingDispatch.DoesNotExist:
            return JsonResponse({"error": "Printing dispatch not found"}, status=404)

@csrf_exempt
def update_printing_progress(request):
    """更新印刷派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")

        try:
            dispatch = PrintingDispatch.objects.filter(work_order_number=work_order_number)
            total_quantity = sum(d.total_quantity for d in dispatch)
            completed_quantity = sum(d.completed_quantity for d in dispatch)
            progress_percentage = (completed_quantity / total_quantity) * 100 if total_quantity > 0 else 0

            PrintingDispatch.objects.filter(work_order_number=work_order_number).update(progress_percentage=progress_percentage)

            return JsonResponse({"message": "Progress updated", "progress": progress_percentage}, status=200)
        except PrintingDispatch.DoesNotExist:
            return JsonResponse({"error": "Printing dispatch not found"}, status=404)

@csrf_exempt
def delete_printing_dispatch(request):
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
