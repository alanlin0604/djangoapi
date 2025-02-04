from django.db import models

class ProductionProgress(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    section = models.CharField(max_length=255)  # 部位名稱
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間
