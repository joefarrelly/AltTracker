# Generated by Django 3.1.7 on 2021-05-12 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0021_altcustom'),
    ]

    operations = [
        migrations.AddField(
            model_name='altcustom',
            name='lastRefresh',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
