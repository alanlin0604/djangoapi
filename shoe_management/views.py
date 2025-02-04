from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Shoe
import json

@csrf_exempt
def add_shoe(request):
    """新增鞋類數據"""
    if request.method == "POST":
        data = json.loads(request.body)
        shoe = Shoe.objects.create(
            nfc_id=data.get("nfc_id"),
            brand=data.get("brand"),
            model=data.get("model"),
            size=data.get("size"),
            material=data.get("material"),
            manufacturer=data.get("manufacturer"),
            origin=data.get("origin"),
        )
        return JsonResponse({"message": "Shoe added successfully", "shoe_id": shoe.id}, status=201)
