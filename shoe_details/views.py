from django.http import JsonResponse
from .models import ShoeDetail

def get_shoe_details(request):
    """獲取指定品牌的所有鞋類詳細資訊"""
    brand_name = request.GET.get("brand", "")
    if not brand_name:
        return JsonResponse({"error": "Missing brand parameter"}, status=400)

    details = list(ShoeDetail.objects.filter(shoe__brand=brand_name).values())
    return JsonResponse(details, safe=False, status=200)
