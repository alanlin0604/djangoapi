from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import OrderMonitor
import json

@csrf_exempt
def get_orders(request):
    """獲取製令單數據"""
    if request.method == "GET":
        orders = OrderMonitor.objects.all().values()
        return JsonResponse(list(orders), safe=False, status=200)
