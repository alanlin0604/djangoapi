from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    model_number = models.CharField(max_length=255)  # 型體編號
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    progress_percentage = models.FloatField(default=0.0)  # 進度百分比

    def __str__(self):
        return self.order_number

class OrderPart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="parts")
    part_name = models.CharField(max_length=255)  # 部位名稱
    material = models.CharField(max_length=255)  # 材料
    size = models.CharField(max_length=50)  # 尺寸
    quantity = models
