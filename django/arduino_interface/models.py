from django.db import models

class ReadData(models.Model):

    humidity = models.FloatField()
    temperature = models.FloatField()
    created = models.DateTimeField()

