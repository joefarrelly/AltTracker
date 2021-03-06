# Generated by Django 3.1.7 on 2021-05-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0039_auto_20210513_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='altprofession',
            name='profession',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Missing'), (171, 'Alchemy'), (164, 'Blacksmithing'), (333, 'Enchanting'), (202, 'Engineering'), (773, 'Inscription'), (755, 'Jewelcrafting'), (165, 'Leatherworking'), (197, 'Tailoring'), (182, 'Herbalism'), (186, 'Mining')], default=0),
        ),
        migrations.AlterField(
            model_name='altcustom',
            name='profession1',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Missing'), (171, 'Alchemy'), (164, 'Blacksmithing'), (333, 'Enchanting'), (202, 'Engineering'), (773, 'Inscription'), (755, 'Jewelcrafting'), (165, 'Leatherworking'), (197, 'Tailoring'), (182, 'Herbalism'), (186, 'Mining')], default=0),
        ),
        migrations.AlterField(
            model_name='altcustom',
            name='profession2',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Missing'), (171, 'Alchemy'), (164, 'Blacksmithing'), (333, 'Enchanting'), (202, 'Engineering'), (773, 'Inscription'), (755, 'Jewelcrafting'), (165, 'Leatherworking'), (197, 'Tailoring'), (182, 'Herbalism'), (186, 'Mining')], default=0),
        ),
        migrations.AlterUniqueTogether(
            name='altprofession',
            unique_together={('alt', 'profession')},
        ),
        migrations.RemoveField(
            model_name='altprofession',
            name='professionName',
        ),
    ]
