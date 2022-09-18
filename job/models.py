from pydoc import describe
from symtable import SymbolTableFactory
from tkinter import CASCADE
from django.db import models

# Create your models here.


JOB_TYPE = (
    ('FULL TIME', 'FULL TIME'),
    ('PART TIME', 'PART TIME'),
)


class job(models.Model):

    title = models.CharField(max_length=50)
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    describtion = models.TextField(max_length=1000)
    publish_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
