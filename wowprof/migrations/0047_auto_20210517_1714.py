# Generated by Django 3.1.7 on 2021-05-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0046_alt_altrealmslug'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='alt',
            constraint=models.UniqueConstraint(fields=('altName', 'altRealmSlug'), name='unique_alt'),
        ),
    ]
