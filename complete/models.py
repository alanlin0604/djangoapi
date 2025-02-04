from django.db import models

class WorkOrder(models.Model):
    workorder_number = models.CharField(max_length=50, unique=True)  # 製令單號
    part = models.CharField(max_length=100)                          # 部位
    size = models.CharField(max_length=20)                           # 尺寸
    quantity = models.IntegerField()                                 # 總數量
    completed_quantity = models.IntegerField(default=0)              # 完成數量
    progress = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)  # 完成進度百分比

    @property
    def incomplete_quantity(self):
        return self.quantity - self.completed_quantity
