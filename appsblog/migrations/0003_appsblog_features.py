# Generated by Django 3.0 on 2020-01-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsblog', '0002_auto_20200107_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='appsblog',
            name='features',
            field=models.TextField(blank=True),
        ),
    ]
