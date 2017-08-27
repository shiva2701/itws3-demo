from django.db import models

class TempSensor(models.Model):
    read_time = models.DateTimeField(auto_now = True)
    reading = models.FloatField()
    
