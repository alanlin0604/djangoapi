from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AttendanceRecord
import json

@csrf_exempt
def get_attendance_data(request):
    """獲取出勤數據"""
    if request.method == "GET":
        date = request.GET.get("date")
        records = AttendanceRecord.objects.filter(date=date).values()
        return JsonResponse(list(records), safe=False, status=200)
