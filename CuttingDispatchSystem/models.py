from django.db import models

class PartDispatch(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    part_name = models.CharField(max_length=255)          # 部位名稱
    material = models.CharField(max_length=255)           # 材料
    size = models.CharField(max_length=255)               # 尺寸
    quantity = models.IntegerField(default=0)             # 數量
    dispatch_progress = models.FloatField(default=0.0)    # 派工進度
    unit = models.CharField(max_length=50, default="")    # 單位
    dispatch_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.work_order_number} - {self.part_name}"
