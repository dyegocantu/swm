from django.db import models

class ReadData(models.Model):

    temperature = models.FloatField()
    humidity = models.FloatField()
    created = models.DateTimeField()

