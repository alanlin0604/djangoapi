from django.db import models

class OrderMonitor(models.Model):
    work_order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    status_percentage = models.FloatField(default=0.0)  # 完成進度百分比
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間
