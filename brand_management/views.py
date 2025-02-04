from django.http import JsonResponse
from .models import Brand

def get_brands(request):
    """獲取品牌列表"""
    if request.method == "GET":
        brands = list(Brand.objects.all().values("name", "logo_url"))
        return JsonResponse(brands, safe=False, status=200)
