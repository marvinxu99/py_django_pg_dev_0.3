# Generated by Django 3.0.7 on 2020-06-30 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transevent',
            name='event_id',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
