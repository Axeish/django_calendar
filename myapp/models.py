# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Entry(models.Model):
	name = models.CharField(max_length=100)
	date = models.DateTimeField()
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name + " "+self.date.strftime('%m/%d/%Y')

# Create your models here.
