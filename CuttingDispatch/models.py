from django.db import models

class DispatchOrder(models.Model):
    work_order_number = models.CharField(max_length=255, unique=True)
    model_number = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    progress = models.FloatField(default=0.0)

    def __str__(self):
        return self.work_order_number
