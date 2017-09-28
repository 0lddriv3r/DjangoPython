# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserRecord(models.Model):
    userName = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.userName + '-' + self.address