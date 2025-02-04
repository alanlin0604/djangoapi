from django.db import models

class HighFrequencyDispatchList(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    dispatch_number = models.CharField(max_length=255)  # 派工單編號
    dispatch_time = models.DateTimeField(null=True, blank=True)  # 派工時間
    print_status = models.CharField(max_length=255, default="未列印")  # 列印狀態
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量

    def __str__(self):
        return f"{self.work_order_number} - {self.dispatch_number}"
