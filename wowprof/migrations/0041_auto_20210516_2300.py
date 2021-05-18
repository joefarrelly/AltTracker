# Generated by Django 3.1.7 on 2021-05-16 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0040_auto_20210514_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('item_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('required_level', models.PositiveSmallIntegerField()),
                ('slot', models.CharField(max_length=20)),
                ('quality', models.CharField(max_length=20)),
                ('armour_type', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'alttracker_equipment',
            },
        ),
        migrations.AlterField(
            model_name='altcustom',
            name='profession1',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Missing'), (171, 'Alchemy'), (164, 'Blacksmithing'), (333, 'Enchanting'), (202, 'Engineering'), (773, 'Inscription'), (755, 'Jewelcrafting'), (165, 'Leatherworking'), (197, 'Tailoring'), (182, 'Herbalism'), (186, 'Mining'), (393, 'Skinning')], default=0),
        ),
        migrations.AlterField(
            model_name='altcustom',
            name='profession2',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Missing'), (171, 'Alchemy'), (164, 'Blacksmithing'), (333, 'Enchanting'), (202, 'Engineering'), (773, 'Inscription'), (755, 'Jewelcrafting'), (165, 'Leatherworking'), (197, 'Tailoring'), (182, 'Herbalism'), (186, 'Mining'), (393, 'Skinning')], default=0),
        ),
        migrations.AlterField(
            model_name='altmedia',
            name='avatar',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='altmedia',
            name='inset',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='altmedia',
            name='main',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='altmedia',
            name='mainRaw',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.CreateModel(
            name='AltEquipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('altEquipmentExpiryDate', models.DateTimeField()),
                ('level', models.PositiveSmallIntegerField()),
                ('stats', models.JSONField()),
                ('alt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wowprof.alt')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wowprof.equipment')),
            ],
            options={
                'db_table': 'alttracker_altequipment',
            },
        ),
    ]
