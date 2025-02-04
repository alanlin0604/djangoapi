from django.db import models

class WorkOrder(models.Model):
    work_order_number = models.CharField(max_length=255, unique=True)
    part = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    progress = models.FloatField(default=0.0)

class NFC(models.Model):
    nfc_id = models.CharField(max_length=255, unique=True)
    linked_to = models.ForeignKey(WorkOrder, on_delete=models.SET_NULL, null=True, blank=True)
