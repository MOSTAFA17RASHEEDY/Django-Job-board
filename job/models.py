from contextlib import nullcontext
from pydoc import describe
from symtable import SymbolTableFactory
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


JOB_TYPE = (
    ('FULL TIME', 'FULL TIME'),
    ('PART TIME', 'PART TIME'),
)


class job(models.Model):
    # owner = models.ForeignKey(
    #   User, related_name="job_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    publish_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class apply(models.Model):
    job = models.ForeignKey(
        job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    coverLeter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
