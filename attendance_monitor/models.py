from django.db import models

class AttendanceRecord(models.Model):
    employee_name = models.CharField(max_length=255)  # 員工名稱
    clock_in_time = models.DateTimeField()  # 上班時間
    clock_out_time = models.DateTimeField(null=True, blank=True)  # 下班時間
    status = models.CharField(max_length=50, choices=[("準時", "準時"), ("遲到", "遲到")])  # 出勤狀況
    date = models.DateField()  # 出勤日期
