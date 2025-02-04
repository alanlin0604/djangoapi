from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import json

@csrf_exempt
def check_existing_users(request):
    """查詢是否已有相同的 email 或 username"""
    if request.method == "GET":
        users = list(User.objects.values("email", "username"))
        return JsonResponse(users, safe=False, status=200)

@csrf_exempt
def register_user(request):
    """處理使用者註冊"""
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        username = data.get("user")
        password = data.get("passwords")

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        User.objects.create(
            email=email,
            username=username,
            password=make_password(password)  # 加密存儲密碼
        )

        return JsonResponse({"message": "User registered successfully"}, status=201)
