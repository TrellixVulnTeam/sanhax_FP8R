# Generated by Django 3.0.2 on 2020-01-07 08:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsblog',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='appsblog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='appsblog',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
