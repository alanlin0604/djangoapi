from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeAttendance, EmployeeProduction
import json
from datetime import datetime

@csrf_exempt
def get_attendance_data(request):
    """獲取員工出勤數據"""
    if request.method == "GET":
        date = request.GET.get("date", "")
        records = EmployeeAttendance.objects.filter(date=date).values()
        return JsonResponse(list(records), safe=False, status=200)

@csrf_exempt
def get_productivity_data(request):
    """獲取員工生產數據"""
    if request.method == "GET":
        name = request.GET.get("name", "")
        date = request.GET.get("date", "")

        records = EmployeeProduction.objects.filter(employee_name=name, date=date).values()
        return JsonResponse(list(records), safe=False, status=200)

@csrf_exempt
def update_productivity_report(request):
    """更新員工生產回報數量"""
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("employee_name")
        date = data.get("date")
        work_order_number = data.get("work_order_number")
        reported_quantity = data.get("reported_quantity")

        try:
            record = EmployeeProduction.objects.get(
                employee_name=name, date=date, work_order_number=work_order_number
            )
            record.reported_quantity += reported_quantity
            record.save()
            return JsonResponse({"message": "Productivity updated"}, status=200)
        except EmployeeProduction.DoesNotExist:
            return JsonResponse({"error": "Record not found"}, status=404)
