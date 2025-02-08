from django.db import models

class PrintingProduction(models.Model):
    order = models.ForeignKey(PrintingOrder, on_delete=models.CASCADE, related_name="productions")
    section = models.CharField(max_length=255)  # 部位名稱
    date = models.DateField()  # 日期
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比

    def __str__(self):
        return f"{self.order.order_number} - {self.section} - {self.date}"
