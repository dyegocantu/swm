# -*- coding: utf-8 -*-

from django.db import models

class ReadData(models.Model):
    humidity = models.FloatField()
    temperature = models.FloatField()
    created = models.DateTimeField()

    def __unicode__(self):
        return u'ReadData(%f, %f, %s)' % \
                (self.humidity, self.temperature, self.created)

