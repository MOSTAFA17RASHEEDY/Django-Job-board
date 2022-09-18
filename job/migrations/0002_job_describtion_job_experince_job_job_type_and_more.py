# Generated by Django 4.1.1 on 2022-09-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='describtion',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='experince',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FULL TIME', 'FULL TIME'), ('PART TIME', 'PART TIME')], default='exit', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='publish_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='vacancy',
            field=models.IntegerField(default=1),
        ),
    ]
