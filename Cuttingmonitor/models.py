from django.db import models

class WorkOrder(models.Model):
    work_order_number = models.CharField(max_length=255, unique=True)  # 製令單號
    upload_date = models.DateTimeField(auto_now_add=True)  # 上傳日期
    last_edit_date = models.DateTimeField(auto_now=True)   # 上次編輯日期

class PartProgress(models.Model):
    work_order = models.ForeignKey(WorkOrder, on_delete=models.CASCADE, related_name="parts")  # 關聯製令單
    part_name = models.CharField(max_length=255)  # 部位名稱
    total_quantity = models.IntegerField(default=0)  # 總數量
    completed_quantity = models.IntegerField(default=0)  # 完成數量
    progress_percentage = models.FloatField(default=0.0)  # 完成進度百分比
    last_updated = models.DateTimeField(auto_now=True)  # 最後更新時間
