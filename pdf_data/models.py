from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    model_number = models.CharField(max_length=255)  # 型體編號
    last_updated = models.DateTimeField(auto_now=True)  # 上次編輯日期
    color = models.CharField(max_length=255, null=True, blank=True)  # 配色
    sole = models.CharField(max_length=255, null=True, blank=True)  # 大底
    last = models.CharField(max_length=255, null=True, blank=True)  # 楦頭
    logo = models.CharField(max_length=255, null=True, blank=True)  # LOGO

    def __str__(self):
        return self.order_number

class OrderPart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="parts")
    part_name = models.CharField(max_length=255)  # 部位名稱
    material = models.CharField(max_length=255)  # 材料
    size = models.CharField(max_length=50)  # 尺寸
    quantity = models.IntegerField(default=0)  # 總數量

    def __str__(self):
        return f"{self.order.order_number} - {self.part_name}"
