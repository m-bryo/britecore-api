# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, transaction

# Create your models here.
from django.utils.text import slugify


class Risk(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()


class Field(models.Model):
    risk = models.ForeignKey(Risk)
    field = models.CharField(max_length=255)
    type = models.CharField(max_length=20, default='text')
    validation = models.CharField(max_length=255, verbose_name='Regex Validator', blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    is_required = models.BooleanField(default=False)

    def save(self, **kwargs):
        super(Field, self).save(**kwargs)
        self.key = "{}_{}".format(self.id, slugify(self.field))


class Option(models.Model):
    field = models.ForeignKey(Field)
    display = models.CharField(max_length=255)


class SubmissionSet(models.Model):
    risk = models.ForeignKey(Field)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)


class SubmissionValue(models.Model):
    set = models.ForeignKey(SubmissionSet)
    field = models.ForeignKey(Field)
    value = models.TextField()

