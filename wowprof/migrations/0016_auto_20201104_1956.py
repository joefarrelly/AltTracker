# Generated by Django 3.1.2 on 2020-11-04 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0015_altquestcompleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='altquestcompleted',
            old_name='AltQuestCompletedExpiryDate',
            new_name='altQuestCompletedExpiryDate',
        ),
    ]
