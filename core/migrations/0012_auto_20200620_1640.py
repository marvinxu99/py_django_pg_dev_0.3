# Generated by Django 3.0.7 on 2020-06-20 23:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200620_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemprice',
            name='active_status_dt_tm',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='effective_dt_tm',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
