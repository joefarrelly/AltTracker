# Generated by Django 3.1.7 on 2021-06-10 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0065_alt_altrealmid'),
    ]

    operations = [
        migrations.AddField(
            model_name='altcustom',
            name='gold',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='altcustom',
            name='location',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
