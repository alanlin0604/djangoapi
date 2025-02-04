from django.db import models

class EmployeeAttendance(models.Model):
    employee_name = models.CharField(max_length=255)  # 員工名稱
    date = models.DateField()  # 出勤日期
    clock_in_time = models.TimeField()  # 上班時間
    clock_out_time = models.TimeField(null=True, blank=True)  # 下班時間
    status = models.CharField(max_length=50, choices=[("準時", "準時"), ("遲到", "遲到")])  # 出勤狀況

    def __str__(self):
        return f"{self.employee_name} - {self.date}"

class EmployeeProduction(models.Model):
    employee_name = models.CharField(max_length=255)  # 員工名稱
    date = models.DateField()  # 生產日期
    work_order_number = models.CharField(max_length=255)  # 製令單號
    part_name = models.CharField(max_length=255)  # 部位名稱
    size = models.CharField(max_length=50)  # 尺寸
    quantity = models.IntegerField(default=0)  # 總數量
    reported_quantity = models.IntegerField(default=0)  # 回報數量

    def __str__(self):
        return f"{self.employee_name} - {self.date} - {self.work_order_number}"
