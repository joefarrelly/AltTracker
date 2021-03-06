# Generated by Django 3.1.2 on 2020-10-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wowprof', '0009_auto_20201012_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alt',
            name='altRace',
            field=models.CharField(choices=[('Human', 'Human'), ('Orc', 'Orc'), ('Dwarf', 'Dwarf'), ('Night Elf', 'Night Elf'), ('Undead', 'Undead'), ('Tauren', 'Tauren'), ('Gnome', 'Gnome'), ('Troll', 'Troll'), ('Goblin', 'Goblin'), ('Blood Elf', 'Blood Elf'), ('Draenei', 'Draenei'), ('Worgen', 'Worgen'), ('Pandaren', 'Pandaren'), ('Nightbourne', 'Nightbourne'), ('Hightmountain Tauren', 'Highmountain Tauren'), ('Void Elf', 'Void Elf'), ('Lightforged Draenei', 'Lightforged Draenei'), ('Zandalari Troll', 'Zandalari Troll'), ('Kul Tiran', 'Kul Tiran'), ('Dark Iron Dwarf', 'Dark Iron Dwarf'), ('Vulpera', 'Vulpera'), ("Mag'ar Orc", 'Maghar Orc'), ('Mechagnome', 'Mechagnome')], max_length=40),
        ),
    ]
