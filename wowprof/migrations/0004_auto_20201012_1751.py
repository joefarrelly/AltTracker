# Generated by Django 3.1.2 on 2020-10-12 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0003_auto_20201012_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alt',
            old_name='altSpec',
            new_name='altRace',
        ),
    ]
