# Generated by Django 5.2.3 on 2025-06-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True)),
                ('due_date', models.DateField(blank=True)),
            ],
        ),
    ]
