from django.db import models

# Create your models here.


class Alt(models.Model):
    altId = models.PositiveIntegerField(primary_key=True)
    altLevel = models.PositiveSmallIntegerField()
    altName = models.CharField(max_length=40)
    altRealm = models.CharField(max_length=40)

    class AltClass(models.TextChoices):
        WARRIOR = 'Warrior'
        PALADIN = 'Paladin'
        HUNTER = 'Hunter'
        ROGUE = 'Rogue'
        PRIEST = 'Priest'
        SHAMAN = 'Shaman'
        MAGE = 'Mage'
        WARLOCK = 'Warlock'
        MONK = 'Monk'
        DRUID = 'Druid'
        DEMON_HUNTER = 'Demon Hunter'
        DEATH_KNIGHT = 'Death Knight'
    altClass = models.CharField(max_length=12, choices=AltClass.choices)

    class AltRace(models.TextChoices):
        HUMAN = 'Human'
        ORC = 'Orc'
        DWARF = 'Dwarf'
        NIGHT_ELF = 'Night Elf'
        UNDEAD = 'Undead'
        TAUREN = 'Tauren'
        GNOME = 'Gnome'
        TROLL = 'Troll'
        GOBLIN = 'Goblin'
        BLOOD_ELF = 'Blood Elf'
        DRAENEI = 'Draenei'
        WORGEN = 'Worgen'
        PANDAREN = 'Pandaren'
        NIGHTBOURNE = 'Nightbourne'
        HIGHMOUNTAIN_TAUREN = 'Highmountain Tauren'
        VOID_ELF = 'Void Elf'
        LIGHTFORGED_DRAENEI = 'Lightforged Draenei'
        ZANDALARI_TROLL = 'Zandalari Troll'
        KUL_TIRAN = 'Kul Tiran'
        DARK_IRON_DWARF = 'Dark Iron Dwarf'
        VULPERA = 'Vulpera'
        MAGHAR_ORC = 'Mag\'ar Orc'
        MECHAGNOME = 'Mechagnome'
    altRace = models.CharField(max_length=20, choices=AltRace.choices)

    class AltGender(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
    altGender = models.CharField(max_length=6, choices=AltGender.choices)

    class AltFaction(models.TextChoices):
        ALLIANCE = 'Alliance'
        HORDE = 'Horde'
    altFaction = models.CharField(max_length=8, choices=AltFaction.choices)
    altExpiryDate = models.DateTimeField()

    class Meta:
        unique_together = (("altName", "altRealm"),)


class AltCustom(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)

    class Mount(models.TextChoices):
        SLOW_GROUND = '1 - Slow Ground'
        FAST_GROUND = '2 - Fast Ground'
        SLOW_FLYING = '3 - Slow Flying'
        FAST_FLYING = '4 - Fast Flying'
    mount = models.CharField(max_length=15, choices=Mount.choices)

    class Garrison(models.TextChoices):
        LEVEL0 = 'Level 0'
        LEVEL1 = 'Level 1'
        LEVEL2 = 'Level 2'
        LEVEL3 = 'Level 3'
    garrison = models.CharField(max_length=7, choices=Garrison.choices)

    class MageTower(models.TextChoices):
        YES = 'Yes'
        NO = 'No'
    mageTower = models.CharField(max_length=3, choices=MageTower.choices)

    class ProfessionOption(models.TextChoices):
        NONE = 'None'
        ALCHEMY = 'Alchemy'
        BLACKSMITHING = 'Blacksmithing'
        ENCHANTING = 'Enchanting'
        ENGINEERING = 'Engineering'
        INSCRIPTION = 'Inscription'
        JEWELCRAFTING = 'Jewelcrafting'
        LEATHERWORKING = 'Leatherworking'
        TAILORING = 'Tailoring'
        HERBALISM = 'Herbalism'
        MINING = 'Mining'
        SKINNING = 'Skinning'
    profession1 = models.CharField(max_length=14, choices=ProfessionOption.choices)
    profession2 = models.CharField(max_length=14, choices=ProfessionOption.choices)


class AltProfession(models.Model):
    alt = models.ForeignKey(Alt, on_delete=models.CASCADE)

    class ProfessionName(models.TextChoices):
        ALCHEMY = 'Alchemy'
        BLACKSMITHING = 'Blacksmithing'
        ENCHANTING = 'Enchanting'
        ENGINEERING = 'Engineering'
        INSCRIPTION = 'Inscription'
        JEWELCRAFTING = 'Jewelcrafting'
        LEATHERWORKING = 'Leatherworking'
        TAILORING = 'Tailoring'
        HERBALISM = 'Herbalism'
        MINING = 'Mining'
        SKINNING = 'Skinning'
    professionName = models.CharField(max_length=14, choices=ProfessionName.choices)
    altProfessionExpiryDate = models.DateTimeField()
    professionData = models.JSONField()

    class Meta:
        unique_together = (("alt", "professionName"),)


class AltAchievement(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altAchievementExpiryDate = models.DateTimeField()
    achievementData = models.JSONField()


class AltQuestCompleted(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altQuestCompletedExpiryDate = models.DateTimeField()
    questCompletedData = models.JSONField()


class AltMedia(models.Model):
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    altMediaExpiryDate = models.DateTimeField()
    avatar = models.CharField(max_length=100)
    inset = models.CharField(max_length=100)
    main = models.CharField(max_length=100)
    mainRaw = models.CharField(max_length=100)


class Requiem(models.Model):
    # reqId = models.PositiveIntegerField(primary_key=True)
    alt = models.OneToOneField(Alt, on_delete=models.CASCADE, primary_key=True)
    # reqLevel = models.PositiveSmallIntegerField()
    reqName = models.CharField(max_length=40)
    reqRealm = models.CharField(max_length=40)
    # class AltClass(models.TextChoices):
    #   WARRIOR = 'Warrior'
    #   PALADIN = 'Paladin'
    #   HUNTER = 'Hunter'
    #   ROGUE = 'Rogue'
    #   PRIEST = 'Priest'
    #   SHAMAN = 'Shaman'
    #   MAGE = 'Mage'
    #   WARLOCK = 'Warlock'
    #   MONK = 'Monk'
    #   DRUID = 'Druid'
    #   DEMON_HUNTER = 'Demon Hunter'
    #   DEATH_KNIGHT = 'Death Knight'
    # reqClass = models.CharField(max_length=12,choices=AltClass.choices)
    reqRank = models.PositiveSmallIntegerField()
    reqExpiryDate = models.DateTimeField()

    # class Meta:
    #   unique_together = (("reqName","reqRealm"),)


class Token(models.Model):
    token = models.CharField(max_length=60)
