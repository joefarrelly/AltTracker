from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Alt(models.Model):
    altId = models.PositiveIntegerField(primary_key=True)
    altLevel = models.PositiveSmallIntegerField()
    altName = models.CharField(max_length=40)
    altRealm = models.CharField(max_length=40)
    altRealmSlug = models.CharField(max_length=40)

    class AltClass(models.IntegerChoices):
        NO_CLASS = 0, _('No Class')
        WARRIOR = 1, _('Warrior')
        PALADIN = 2, _('Paladin')
        HUNTER = 3, _('Hunter')
        ROGUE = 4, _('Rogue')
        PRIEST = 5, _('Priest')
        DEATH_KNIGHT = 6, _('Death Knight')
        SHAMAN = 7, _('Shaman')
        MAGE = 8, _('Mage')
        WARLOCK = 9, _('Warlock')
        MONK = 10, _('Monk')
        DRUID = 11, _('Druid')
        DEMON_HUNTER = 12, _('Demon Hunter')
    altClass = models.PositiveSmallIntegerField(choices=AltClass.choices, default=AltClass.NO_CLASS)

    class AltRace(models.IntegerChoices):
        NO_RACE = 0, _('No Race')
        HUMAN = 1, _('Human')
        ORC = 2, _('Orc')
        DWARF = 3, _('Dwarf')
        NIGHT_ELF = 4, _('Night Elf')
        UNDEAD = 5, _('Undead')
        TAUREN = 6, _('Tauren')
        GNOME = 7, _('Gnome')
        TROLL = 8, _('Troll')
        GOBLIN = 9, _('Goblin')
        BLOOD_ELF = 10, _('Blood Elf')
        DRAENEI = 11, _('Draenei')
        WORGEN = 22, _('Worgen')
        PANDAREN_NEUTRAL = 24, _('Pandaren')
        PANDAREN_ALLIANCE = 25, _('Pandaren')
        PANDAREN_HORDE = 26, _('Pandaren')
        NIGHTBOURNE = 27, _('Nightbourne')
        HIGHMOUNTAIN_TAUREN = 28, _('Highmountain Tauren')
        VOID_ELF = 29, _('Void Elf')
        LIGHTFORGED_DRAENEI = 30, _('Lightforged Draenei')
        ZANDALARI_TROLL = 31, _('Zandalari Troll')
        KUL_TIRAN = 32, _('Kul Tiran')
        DARK_IRON_DWARF = 34, _('Dark Iron Dwarf')
        VULPERA = 35, _('Vulpera')
        MAGHAR_ORC = 36, _('Mag\'ar Orc')
        MECHAGNOME = 37, _('Mechagnome')
    altRace = models.PositiveSmallIntegerField(choices=AltRace.choices, default=AltRace.NO_RACE)

    altGender = models.CharField(max_length=6)
    altFaction = models.CharField(max_length=10)
    altExpiryDate = models.DateTimeField()

    class Meta:
        db_table = 'alttracker_alt'
        constraints = [
            models.UniqueConstraint(fields=['altName', 'altRealmSlug'], name='unique_alt')
        ]

    def __str__(self):
        return '%s - %s' % (self.altName, self.altRealm)


class AltCustom(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)

    NOT_LEARNT = 0
    SLOW_GROUND = 1
    FAST_GROUND = 2
    SLOW_FLYING = 3
    FAST_FLYING = 4
    MOUNT = (
        (NOT_LEARNT, 'No Riding Skill'),
        (SLOW_GROUND, 'Slow Ground'),
        (FAST_GROUND, 'Fast Ground'),
        (SLOW_FLYING, 'Slow Flying'),
        (FAST_FLYING, 'Fast Flying'),
    )
    mount = models.PositiveSmallIntegerField(choices=MOUNT, default=SLOW_GROUND)

    LEVEL0 = 0
    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    GARRISON = (
        (LEVEL0, 'Not Built'),
        (LEVEL1, 'Level 1'),
        (LEVEL2, 'Level 2'),
        (LEVEL3, 'Level 3'),
    )
    garrison = models.PositiveSmallIntegerField(choices=GARRISON, default=LEVEL0)

    NO = 0
    YES = 1
    MAGE_TOWER = (
        (NO, 'No'),
        (YES, 'Yes'),
    )
    mageTower = models.PositiveSmallIntegerField(choices=MAGE_TOWER, default=NO)

    class Profession(models.IntegerChoices):
        MISSING = 0, _('Missing')
        ALCHEMY = 171, _('Alchemy')
        BLACKSMITHING = 164, _('Blacksmithing')
        ENCHANTING = 333, _('Enchanting')
        ENGINEERING = 202, _('Engineering')
        INSCRIPTION = 773, _('Inscription')
        JEWELCRAFTING = 755, _('Jewelcrafting')
        LEATHERWORKING = 165, _('Leatherworking')
        TAILORING = 197, _('Tailoring')
        HERBALISM = 182, _('Herbalism')
        MINING = 186, _('Mining')
        SKINNING = 393, _('Skinning')
    profession1 = models.PositiveSmallIntegerField(choices=Profession.choices, default=Profession.MISSING)
    profession2 = models.PositiveSmallIntegerField(choices=Profession.choices, default=Profession.MISSING)

    lastRefresh = models.DateTimeField()

    class Meta:
        db_table = 'alttracker_altcustom'

    def __str__(self):
        return '%s - %s' % (self.alt.altName, self.alt.altRealm)


class AltProfession(models.Model):
    alt = models.ForeignKey(Alt, on_delete=models.CASCADE)

    class Profession(models.IntegerChoices):
        MISSING = 0, _('Missing')
        ALCHEMY = 171, _('Alchemy')
        BLACKSMITHING = 164, _('Blacksmithing')
        ENCHANTING = 333, _('Enchanting')
        ENGINEERING = 202, _('Engineering')
        INSCRIPTION = 773, _('Inscription')
        JEWELCRAFTING = 755, _('Jewelcrafting')
        LEATHERWORKING = 165, _('Leatherworking')
        TAILORING = 197, _('Tailoring')
        HERBALISM = 182, _('Herbalism')
        MINING = 186, _('Mining')
    profession = models.PositiveSmallIntegerField(choices=Profession.choices, default=Profession.MISSING)

    altProfessionExpiryDate = models.DateTimeField()
    professionData = models.JSONField()

    class Meta:
        db_table = 'alttracker_altprofession'
        constraints = [
            models.UniqueConstraint(fields=['alt', 'profession'], name='unique_profession')
        ]

    def __str__(self):
        return '%s - %s : %s' % (self.alt.altName, self.alt.altRealm, self.get_profession_display())


class AltAchievement(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altAchievementExpiryDate = models.DateTimeField()
    achievementData = models.JSONField()

    class Meta:
        db_table = 'alttracker_altachievement'

    def __str__(self):
        return '%s - %s' % (self.alt.altName, self.alt.altRealm)


class AltQuestCompleted(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altQuestCompletedExpiryDate = models.DateTimeField()
    questCompletedData = models.JSONField()

    class Meta:
        db_table = 'alttracker_altquestcompleted'

    def __str__(self):
        return '%s - %s' % (self.alt.altName, self.alt.altRealm)


class AltMedia(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altMediaExpiryDate = models.DateTimeField()
    avatar = models.CharField(max_length=100, default=None)
    inset = models.CharField(max_length=100, default=None)
    main = models.CharField(max_length=100, default=None)
    mainRaw = models.CharField(max_length=100, default=None)

    class Meta:
        db_table = 'alttracker_altmedia'

    def __str__(self):
        return '%s - %s' % (self.alt.altName, self.alt.altRealm)


class Equipment(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    # required_level = models.CharField(max_length=80)
    slot = models.CharField(max_length=20)
    quality = models.CharField(max_length=20)
    armour_type = models.CharField(max_length=20)
    icon = models.CharField(max_length=100)

    class Meta:
        db_table = 'alttracker_equipment'

    def __str__(self):
        return '%s' % (self.name)


class AltEquipment(models.Model):
    alt = models.ForeignKey(Alt, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    altEquipmentExpiryDate = models.DateTimeField()
    item_level = models.PositiveSmallIntegerField()
    stats = models.JSONField()
    slot = models.CharField(max_length=20)

    class Meta:
        db_table = 'alttracker_altequipment'

    def __str__(self):
        return '%s' % (self.alt.altName)


######################################################################################
# NO LONGER USED

# class Requiem(models.Model):
#     # reqId = models.PositiveIntegerField(primary_key=True)
#     alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
#     # reqLevel = models.PositiveSmallIntegerField()
#     reqName = models.CharField(max_length=40)
#     reqRealm = models.CharField(max_length=40)
#     # class AltClass(models.TextChoices):
#     #   WARRIOR = 'Warrior'
#     #   PALADIN = 'Paladin'
#     #   HUNTER = 'Hunter'
#     #   ROGUE = 'Rogue'
#     #   PRIEST = 'Priest'
#     #   SHAMAN = 'Shaman'
#     #   MAGE = 'Mage'
#     #   WARLOCK = 'Warlock'
#     #   MONK = 'Monk'
#     #   DRUID = 'Druid'
#     #   DEMON_HUNTER = 'Demon Hunter'
#     #   DEATH_KNIGHT = 'Death Knight'
#     # reqClass = models.CharField(max_length=12,choices=AltClass.choices)
#     reqRank = models.PositiveSmallIntegerField()
#     reqExpiryDate = models.DateTimeField()

#     # class Meta:
#     #   unique_together = (("reqName","reqRealm"),)


# class Token(models.Model):
#     token = models.CharField(max_length=60)

######################################################################################
