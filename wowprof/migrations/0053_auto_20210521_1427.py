# Generated by Django 3.1.7 on 2021-05-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0052_auto_20210517_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='altequipment',
            name='enchants',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='altequipment',
            name='sockets',
            field=models.JSONField(default=[]),
            preserve_default=False,
        ),
    ]