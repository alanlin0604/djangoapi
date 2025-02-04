from django.db import models

class HighFrequencyWorkOrder(models.Model):
    work_order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    dispatch_number = models.CharField(max_length=255)  # 派工單編號
    section = models.CharField(max_length=255)  # 部位名稱
    material = models.CharField(max_length=255)  # 材料名稱
    size = models.CharField(max_length=50)  # 尺寸
    quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    dispatch_time = models.DateTimeField(null=True, blank=True)  # 派工時間

    def __str__(self):
        return f"{self.work_order_number} - {self.dispatch_number}"
