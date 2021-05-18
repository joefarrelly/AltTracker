# Generated by Django 3.1.7 on 2021-05-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0025_auto_20210512_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altcustom',
            name='mount',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Slow Ground'), (1, 'Fast Ground'), (2, 'Slow Flying'), (3, 'Fast Flying')], default=0),
        ),
    ]
