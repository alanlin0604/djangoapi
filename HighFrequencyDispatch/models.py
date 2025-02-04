from django.db import models

class HighFrequencyDispatch(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    progress_percentage = models.FloatField(default=0.0)  # 派工進度
    section = models.CharField(max_length=255, null=True, blank=True)  # 部位名稱
    material = models.CharField(max_length=255, null=True, blank=True)  # 材料名稱
    dispatch_time = models.DateTimeField(auto_now_add=True)  # 派工時間
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間

    def __str__(self):
        return f"{self.work_order_number} - {self.section if self.section else '未指定部位'}"
