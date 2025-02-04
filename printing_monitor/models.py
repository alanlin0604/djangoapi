from django.db import models

class PrintingOrder(models.Model):
    order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    model_number = models.CharField(max_length=255)  # 型體編號
    upload_time = models.DateTimeField(auto_now_add=True)  # 上傳時間
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比

    def __str__(self):
        return self.order_number
