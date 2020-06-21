# Generated by Django 3.0.7 on 2020-06-20 21:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200620_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdefinition',
            name='create_dt_tm',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 21, 37, 22, 205025, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemdefinition',
            name='updt_dt_tm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='itemidentifier',
            name='updt_dt_tm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='create_dt_tm',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 21, 37, 22, 209954, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itemprice',
            name='updt_dt_tm',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='itempricehist',
            name='create_dt_tm',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 21, 37, 22, 213919, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='itempricehist',
            name='updt_dt_tm',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
