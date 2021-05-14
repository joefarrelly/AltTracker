# Generated by Django 3.1.7 on 2021-05-13 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0034_auto_20210513_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alt',
            name='altRace',
            field=models.PositiveSmallIntegerField(choices=[(0, 'No Race'), (1, 'Human'), (2, 'Orc'), (3, 'Dwarf'), (4, 'Night Elf'), (5, 'Undead'), (6, 'Tauren'), (7, 'Gnome'), (8, 'Troll'), (9, 'Goblin'), (10, 'Blood Elf'), (11, 'Draenei'), (12, 'Worgen'), (13, 'Pandaren'), (14, 'Nightbourne'), (15, 'Highmountain Tauren'), (16, 'Void Elf'), (17, 'Lightforged Draenei'), (18, 'Zandalari Troll'), (19, 'Kul Tiran'), (20, 'Dark Iron Dwarf'), (21, 'Vulpera'), (22, "Mag'ar Orc"), (23, 'Mechagnome')], default=0),
        ),
    ]
