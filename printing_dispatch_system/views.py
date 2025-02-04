from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PrintingDispatch
import json

@csrf_exempt
def direct_dispatch(request):
    """直接派工"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        section = data.get("section")
        size = data.get("size")
        total_quantity = data.get("total_quantity")

        dispatch = PrintingDispatch.objects.create(
            work_order_number=work_order_number,
            dispatch_number=f"PD-{work_order_number}-{section}",
            section=section,
            size=size,
            total_quantity=total_quantity,
            completed_quantity=0,
            progress_percentage=0.0,
        )
        return JsonResponse({"message": "Dispatch created", "dispatch_number": dispatch.dispatch_number}, status=201)

@csrf_exempt
def update_progress(request):
    """更新派工進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")

        try:
            dispatches = PrintingDispatch.objects.filter(work_order_number=work_order_number)
            total_quantity = sum(d.total_quantity for d in dispatches)
            completed_quantity = sum(d.completed_quantity for d in dispatches)
            progress_percentage = (completed_quantity / total_quantity) * 100 if total_quantity > 0 else 0

            PrintingDispatch.objects.filter(work_order_number=work_order_number).update(progress_percentage=progress_percentage)

            return JsonResponse({"message": "Progress updated", "progress": progress_percentage}, status=200)
        except PrintingDispatch.DoesNotExist:
            return JsonResponse({"error": "Printing dispatch not found"}, status=404)
