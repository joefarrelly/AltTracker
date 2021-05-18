# Generated by Django 3.1.7 on 2021-05-17 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0049_auto_20210517_1723'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='alt',
            name='unique_alt',
        ),
        migrations.AddConstraint(
            model_name='alt',
            constraint=models.UniqueConstraint(fields=('altName', 'altRealm'), name='unique_alt'),
        ),
    ]