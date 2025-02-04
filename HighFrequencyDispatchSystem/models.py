from django.db import models

class HighFrequencyDispatch(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    dispatch_number = models.CharField(max_length=255)  # 派工單編號
    section = models.CharField(max_length=255)  # 部位名稱
    size = models.CharField(max_length=50)  # 尺寸
    quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比
    dispatch_time = models.DateTimeField(auto_now_add=True)  # 派工時間
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間

    def __str__(self):
        return f"{self.work_order_number} - {self.dispatch_number}"
