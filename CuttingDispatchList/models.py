from django.db import models

class DispatchList(models.Model):
    work_order_number = models.CharField(max_length=255)
    part = models.CharField(max_length=255)
    dispatch_time = models.DateTimeField()
    print_status = models.CharField(max_length=255, default='尚未列印')
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return self.work_order_number
