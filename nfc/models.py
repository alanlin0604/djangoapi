from django.db import models

class NFCID(models.Model):
    nfcid = models.BigIntegerField(unique=True)
    ID = models.IntegerField(default=0)
    usingstate = models.CharField(max_length=20, default="未使用")

    def __str__(self):
        return str(self.nfcid)
