from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WorkOrder, PartProgress
import json

@csrf_exempt
def get_work_order_progress(request):
    """獲取製令單的部位進度列表"""
    if request.method == "GET":
        work_order_number = request.GET.get("workorderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)

        try:
            work_order = WorkOrder.objects.get(work_order_number=work_order_number)
            parts = PartProgress.objects.filter(work_order=work_order).values(
                "part_name", "total_quantity", "completed_quantity", "progress_percentage", "last_updated"
            )
            return JsonResponse(list(parts), safe=False, status=200)
        except WorkOrder.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)

@csrf_exempt
def update_completed_quantity(request):
    """更新某部位的完成數量和進度"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        part_name = data.get("part_name")
        completed_quantity = data.get("completed_quantity", 0)

        try:
            work_order = WorkOrder.objects.get(work_order_number=work_order_number)
            part = PartProgress.objects.get(work_order=work_order, part_name=part_name)

            # 更新完成數量與進度百分比
            part.completed_quantity = completed_quantity
            part.progress_percentage = (completed_quantity / part.total_quantity) * 100 if part.total_quantity > 0 else 0
            part.save()

            return JsonResponse({"message": "Progress updated"}, status=200)
        except (WorkOrder.DoesNotExist, PartProgress.DoesNotExist):
            return JsonResponse({"error": "Work order or part not found"}, status=404)

@csrf_exempt
def get_part_progress(request):
    """獲取某製令單中所有部位的進度數據"""
    if request.method == "GET":
        work_order_number = request.GET.get("workorderNumber", "")
        if not work_order_number:
            return JsonResponse({"error": "Missing work order number"}, status=400)

        try:
            parts = PartProgress.objects.filter(work_order__work_order_number=work_order_number).values(
                "part_name", "progress_percentage"
            )
            return JsonResponse(list(parts), safe=False, status=200)
        except WorkOrder.DoesNotExist:
            return JsonResponse({"error": "Work order not found"}, status=404)

@csrf_exempt
def create_work_order(request):
    """新增製令單及相關部位進度記錄"""
    if request.method == "POST":
        data = json.loads(request.body)
        work_order_number = data.get("work_order_number")
        parts = data.get("parts", [])

        try:
            work_order = WorkOrder.objects.create(work_order_number=work_order_number)

            for part in parts:
                PartProgress.objects.create(
                    work_order=work_order,
                    part_name=part["part_name"],
                    total_quantity=part.get("total_quantity", 0),
                    completed_quantity=part.get("completed_quantity", 0),
                )

            return JsonResponse({"message": "Work order created"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
