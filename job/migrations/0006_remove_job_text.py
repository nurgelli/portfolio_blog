# Generated by Django 5.2.3 on 2025-07-01 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='text',
        ),
    ]
