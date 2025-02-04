from django.db import models

class QualityControl(models.Model):
    order_number = models.CharField(max_length=255)  # 製令單號
    section = models.CharField(max_length=255)  # 部位名稱
    process_type = models.CharField(max_length=50, choices=[("Cutting", "剪裁"), ("Printing", "印刷"), ("HighFrequency", "高周波")])  # 生產流程
    defect_count = models.IntegerField(default=0)  # 不良數量
    defect_rate = models.FloatField(default=0.0)  # 不良率百分比
    recorded_at = models.DateTimeField(auto_now=True)  # 記錄時間

    def __str__(self):
        return f"{self.order_number} - {self.section} ({self.process_type})"
