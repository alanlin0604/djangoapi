from django.db import models

class Shoe(models.Model):
    nfc_id = models.CharField(max_length=255, unique=True)  # NFC ID
    brand = models.CharField(max_length=255)  # 品牌
    model = models.CharField(max_length=255)  # 型號
    size = models.CharField(max_length=50)  # 尺寸
    material = models.CharField(max_length=255)  # 材質
    manufacturer = models.CharField(max_length=255)  # 製造商
    origin = models.CharField(max_length=255)  # 產地

    def __str__(self):
        return f"{self.brand} - {self.model} ({self.nfc_id})"
