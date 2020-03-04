# Generated by Django 2.2.8 on 2020-01-24 11:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authanalitics', '0011_auto_20200124_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aacharacter',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='zkill', to='eveonline.EveCharacter'),
        ),
        migrations.AlterField(
            model_name='aacharacter',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 11, 9, 13, 829574)),
        ),
        migrations.AlterField(
            model_name='aazkillmonth',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 14, 11, 9, 13, 830851)),
        ),
    ]