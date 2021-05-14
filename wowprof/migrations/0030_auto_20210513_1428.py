# Generated by Django 3.1.7 on 2021-05-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0029_auto_20210513_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='altcustom',
            name='mount',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No Riding Skill'), (1, 'Slow Ground'), (2, 'Fast Ground'), (3, 'Slow Flying'), (4, 'Fast Flying')], default=1),
        ),
    ]
