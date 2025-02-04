from django.db import models

class PrintingOrder(models.Model):
    work_order_number = models.CharField(max_length=255)  # 製令單號
    dispatch_number = models.CharField(max_length=255, unique=True)  # 派工單號
    section = models.CharField(max_length=255)  # 部位名稱
    size = models.CharField(max_length=50)  # 尺寸
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    dispatch_time = models.DateTimeField(null=True, blank=True)  # 派工時間
    nfc_tag = models.CharField(max_length=255, null=True, blank=True)  # 綁定 NFC

    def __str__(self):
        return f"{self.work_order_number} - {self.dispatch_number}"

class PrintingMaterial(models.Model):
    work_order_number = models.ForeignKey(PrintingOrder, on_delete=models.CASCADE, related_name="materials")
    part_name = models.CharField(max_length=255)  # 部位名稱
    material_name = models.CharField(max_length=255)  # 材料
    quantity = models.IntegerField(default=0)  # 材料總數量

    def __str__(self):
        return f"{self.work_order_number} - {self.part_name}"
