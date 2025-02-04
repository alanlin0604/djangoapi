from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)  # 唯一電子郵件
    username = models.CharField(max_length=255, unique=True)  # 使用者名稱
    password = models.CharField(max_length=255)  # 密碼 (加密存儲)

    def __str__(self):
        return self.username
