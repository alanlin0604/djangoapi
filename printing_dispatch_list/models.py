from django.db import models

class PrintingDispatch(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    dispatch_number = models.CharField(max_length=255, unique=True)  # 派工單號
    dispatch_time = models.DateTimeField(null=True, blank=True)  # 派工時間
    print_status = models.CharField(max_length=50, default="未列印")  # 列印狀態
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    nfc_tag = models.CharField(max_length=255, null=True, blank=True)  # 綁定 NFC

    def __str__(self):
        return f"{self.work_order_number} - {self.dispatch_number}"
