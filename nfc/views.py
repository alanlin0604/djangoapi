from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import NFCID
import json

@csrf_exempt
def nfctag_create(request):
    if request.method == "GET":
        nfc_ids = list(NFCID.objects.all().values())
        max_id = max([n['nfcid'] for n in nfc_ids], default=0)
        for i in range(1, 101):
            new_nfcid = max_id + i
            NFCID.objects.create(nfcid=new_nfcid, usingstate="未使用")
        return JsonResponse({"message": "NFC tags created"}, status=200)

@csrf_exempt
def nfc_summon(request):
    if request.method == "POST":
        data = json.loads(request.body)
        NFCID.objects.create(nfcid=data['nfcid'], ID=data.get('ID', 0), usingstate="未使用")
        return JsonResponse({"message": f"NFC tag {data['nfcid']} created"}, status=200)

@csrf_exempt
def nfctag_change(request):
    if request.method == "POST":
        NFCID.objects.filter(usingstate="未使用").update(usingstate="使用中")
        return JsonResponse({"message": "Updated all unused NFC tags to '使用中'"}, status=200)

@csrf_exempt
def nfctag_delete(request):
    if request.method == "POST":
        NFCID.objects.all().delete()
        return JsonResponse({"message": "All NFC tags deleted"}, status=200)

@csrf_exempt
def return_user(request):
    if request.method == "GET":
        username = request.GET.get('Username')
        # Add any logic here for the `AddPunchIn` equivalent
        return JsonResponse({"message": f"User {username} processed"}, status=200)
