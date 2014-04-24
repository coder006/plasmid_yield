from django.db import models

class biosop(models.Model):
    culture_volume = models.FloatField(default = None)
    form = models.FloatField(default = None)
    volume_buffer1 = models.FloatField(default  = None)
    volume_buffer2 = models.FloatField(default = None)
    volume_buffer3 = models.FloatField(default  = None)
    volume_resuspension = models.FloatField(default = None)
    const = models.IntegerField(default = None)
    pl_yield = models.FloatField(default = None)