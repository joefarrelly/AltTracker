# Generated by Django 3.1.7 on 2021-05-21 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0059_auto_20210521_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altcustom',
            name='shadowmourne',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No'), (1, 'Yes'), (2, 'N/A'), (3, 'No(Q)')], default=2),
        ),
    ]
