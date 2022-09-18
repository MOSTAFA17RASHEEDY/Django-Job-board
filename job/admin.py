from atexit import register
from django.contrib import admin

# Register your models here.
from .models import job
from .models import category
admin.site.register(job)
admin.site.register(category)
