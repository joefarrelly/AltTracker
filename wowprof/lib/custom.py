import requests
import environ
import datetime
from django.utils import timezone
from wowprof.models import *

from urllib.parse import quote

from ratelimit import limits, sleep_and_retry

SECOND = 1

env = environ.Env()
environ.Env.read_env()

BLIZZ_CLIENT = env("BLIZZ_CLIENT")
BLIZZ_SECRET = env("BLIZZ_SECRET")


def my_func(foo, bar):
    print(foo)
    print(bar)
    print("Job in a queue done")
    return


def getToken(BLIZZ_CLIENT, BLIZZ_SECRET):
    url = 'https://eu.battle.net/oauth/token?grant_type=client_credentials'
    myobj = {'client_id': BLIZZ_CLIENT, 'client_secret': BLIZZ_SECRET}
    x = requests.post(url, data=myobj)
    token = x.json()['access_token']
    return token


def get_alt_data_temp(alts):
    for alt in alts:
        alt_obj = Alt.objects.get(altId=alt)
        getAltData(((alt_obj.altName).replace('\'', '')).lower(), ((alt_obj.altRealm).replace('\'', '')).lower(), alt_obj)


@sleep_and_retry
@limits(calls=100, period=SECOND)
def getAltData(name, realm, alt_obj):
    print(name + '-' + realm)
    client_token = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
    params = {'access_token': client_token, 'namespace': 'profile-eu', 'locale': 'en_US'}
    urls = [
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/professions',
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/achievements',
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/quests/completed',
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/quests',
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/character-media',
        'https://eu.api.blizzard.com/profile/wow/character/' + realm + '/' + quote(name) + '/equipment'
    ]
    mount = garrison = mage_tower = shadowmourne = 0
    current_professions = []
    for url in urls:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            if 'professions' in url:
                try:
                    # current_professions = []
                    data = response.json()['primaries']
                    for profession in data:
                        try:
                            obj = AltProfession.objects.get(alt=alt_obj, profession=profession['profession']['id'])
                            obj.altProfessionExpiryDate = timezone.now() + datetime.timedelta(days=30)
                            obj.professionData = profession['tiers']
                            obj.save()
                        except AltProfession.DoesNotExist:
                            AltProfession.objects.create(
                                alt=alt_obj,
                                profession=profession['profession']['id'],
                                altProfessionExpiryDate=timezone.now() + datetime.timedelta(days=30),
                                professionData=(profession['tiers'])
                            )
                        finally:
                            current_professions.append(profession['profession']['id'])
                    existing_professions = AltProfession.objects.filter(alt=alt_obj)
                    for profession in existing_professions:
                        if not (profession.profession in current_professions):
                            profession.delete()
                        else:
                            pass
                except KeyError:
                    print(name + '-' + realm + ' has no professions data')
            elif 'achievements' in url:
                try:
                    # mount = garrison = 0
                    data = response.json()['achievements']
                    for achievement in data:
                        # if achievement['id'] == 10459 and achievement['criteria']['is_completed']:
                        #     balance_of_power += 1
                        if achievement['id'] == 891 and achievement['criteria']['is_completed']:  # riding skill slow ground
                            mount += 1
                        elif achievement['id'] == 889 and achievement['criteria']['is_completed']:  # riding skill fast ground
                            mount += 1
                        elif achievement['id'] == 890 and achievement['criteria']['is_completed']:  # riding skill slow flying
                            mount += 1
                        elif achievement['id'] == 5180 and achievement['criteria']['is_completed']:  # riding skill fast flying
                            mount += 1
                        elif (achievement['id'] == 9100 or achievement['id'] == 9545) and achievement['criteria']['is_completed']:  # garrison level 2, alliance(9100) and horde(9545)
                            garrison += 1
                        elif (achievement['id'] == 9101 or achievement['id'] == 9546) and achievement['criteria']['is_completed']:  # garrison level 3, alliance(9101) and horde(9546)
                            garrison += 1
                    try:
                        obj = AltAchievement.objects.get(alt=alt_obj)
                        obj.achievementData = data
                        obj.altAchievementExpiryDate = timezone.now() + datetime.timedelta(days=30)
                        obj.save()
                    except AltAchievement.DoesNotExist:
                        AltAchievement.objects.create(
                            alt=alt_obj,
                            achievementData=response.json()['achievements'],
                            altAchievementExpiryDate=timezone.now() + datetime.timedelta(days=30),
                        )
                except KeyError:
                    print(name + '-' + realm + ' has no achievement data')
            elif 'quests/completed' in url:
                try:
                    # mage_tower = 0
                    data = response.json()['quests']
                    for quest in data:
                        if quest['id'] == 36848:
                            mage_tower += 1
                        if quest['id'] == 24914:
                            shadowmourne += 1
                        # if quest['id'] == 43533:
                        #     balance_of_power += 1
                    try:
                        obj = AltQuestCompleted.objects.get(alt=alt_obj)
                        obj.questCompletedData = data
                        obj.altQuestCompletedExpiryDate = timezone.now() + datetime.timedelta(days=30)
                        obj.save()
                    except AltQuestCompleted.DoesNotExist:
                        AltQuestCompleted.objects.create(
                            alt=alt_obj,
                            questCompletedData=response.json()['quests'],
                            altQuestCompletedExpiryDate=timezone.now() + datetime.timedelta(days=30),
                        )
                except KeyError:
                    print(name + '-' + realm + ' has no quest data')
            elif 'quests' in url:
                try:
                    data = response.json()['in_progress']
                    for quest in data:
                        if quest['id'] == 24548:
                            shadowmourne = 3
                except KeyError:
                    print(name + '-' + realm + ' has no active quest data')
            elif 'character-media' in url:
                try:
                    avatar = inset = main = mainRaw = 'No media'
                    for img in response.json()['assets']:
                        if img['key'] == 'avatar':
                            avatar = img['value']
                        elif img['key'] == 'inset':
                            inset = img['value']
                        elif img['key'] == 'main':
                            main = img['value']
                        elif img['key'] == 'main-raw':
                            mainRaw = img['value']
                    try:
                        obj = AltMedia.objects.get(alt=alt_obj)
                        obj.avatar = avatar
                        obj.inset = inset
                        obj.main = main
                        obj.mainRaw = mainRaw
                        obj.altMediaExpiryDate = timezone.now() + datetime.timedelta(days=30)
                        obj.save()
                    except AltMedia.DoesNotExist:
                        AltMedia.objects.create(
                            alt=alt_obj,
                            avatar=avatar,
                            inset=inset,
                            main=main,
                            mainRaw=mainRaw,
                            altMediaExpiryDate=timezone.now() + datetime.timedelta(days=30),
                        )
                except KeyError:
                    print(name + '-' + realm + ' has no media data')
            elif 'equipment' in url:
                try:
                    data = response.json()['equipped_items']
                    print(len(data))
                    for item in data:
                        try:
                            obj = Equipment.objects.get(item_id=item['item']['id'])
                            obj.name = item['name']
                            obj.slot = item['slot']['type']
                            # obj.quality = item['quality']['name']
                            obj.armour_type = item['item_subclass']['name']
                            # obj.icon = media_url
                            obj.save()
                        except Equipment.DoesNotExist:
                            media_url_response = requests.get('https://eu.api.blizzard.com/data/wow/media/item/' + str(item['item']['id']), params={'access_token': client_token, 'namespace': 'static-eu', 'locale': 'en_US'})
                            if media_url_response.status_code == 200:
                                try:
                                    media_url = media_url_response.json()['assets'][0]['value']
                                except KeyError:
                                    print('Could not locate equipment icon')
                                    media_url = 'Icon not found'
                            else:
                                media_url = 'Icon not found2'
                            obj = Equipment.objects.create(
                                item_id=item['item']['id'],
                                name=item['name'],
                                # required_level=required_level,
                                slot=item['slot']['type'],
                                # quality=item['quality']['name'],
                                armour_type=item['item_subclass']['name'],
                                icon=media_url
                            )
                        if 'stats' in item:
                            stats = item['stats']
                        else:
                            stats = 'None'
                        if 'sockets' in item:
                            sockets = item['sockets']
                        else:
                            sockets = []
                        if 'enchantments' in item:
                            enchants = item['enchantments']
                        else:
                            enchants = []
                        if 'spells' in item:
                            spells = item['spells']
                        else:
                            spells = []
                        if 'azerite_details' in item:
                            azerite = item['azerite_details']
                        else:
                            azerite = []
                        try:
                            obj1 = AltEquipment.objects.get(alt=alt_obj, slot=item['slot']['type'])
                            obj1.equipment = obj
                            obj1.item_level = item['level']['value']
                            obj1.stats = stats
                            obj1.sockets = sockets
                            obj1.quality = item['quality']['name']
                            obj1.enchants = enchants
                            obj1.spells = spells
                            obj1.azerite = azerite
                            obj1.altEquipmentExpiryDate = timezone.now() + datetime.timedelta(days=30)
                            obj1.save()
                        except AltEquipment.DoesNotExist:
                            AltEquipment.objects.create(
                                alt=alt_obj,
                                equipment=obj,
                                item_level=item['level']['value'],
                                stats=stats,
                                sockets=sockets,
                                quality=item['quality']['name'],
                                enchants=enchants,
                                spells=spells,
                                azerite=azerite,
                                altEquipmentExpiryDate=timezone.now() + datetime.timedelta(days=30),
                                slot=item['slot']['type']
                            )
                except KeyError:
                    print(name + '-' + realm + ' has no equipment data')
                    print(KeyError)
        response.close()
    if alt_obj.altFaction == 'Horde':
        mage_tower = 2
    if (alt_obj.altClass != 1) and (alt_obj.altClass != 2) and (alt_obj.altClass != 6):
        shadowmourne = 2
    try:
        obj = AltCustom.objects.get(alt=alt_obj)
        obj.mount = mount
        obj.garrison = garrison + 1
        obj.mageTower = mage_tower
        obj.shadowmourne = shadowmourne
        # obj.balance_of_power = balance_of_power
        # obj.profession1 = getattr(AltCustom, (next(iter(current_professions[0:1] or []), 'Missing')).upper())
        obj.profession1 = next(iter(current_professions[0:1] or []), 0)
        # obj.profession2 = getattr(AltCustom, (next(iter(current_professions[1:2] or []), 'Missing')).upper())
        obj.profession2 = next(iter(current_professions[1:2] or []), 0)
        obj.lastRefresh = timezone.now()
        obj.save()
    except AltCustom.DoesNotExist:
        AltCustom.objects.create(
            alt=alt_obj,
            mount=mount,
            garrison=garrison + 1,
            mageTower=mage_tower,
            shadowmourne=shadowmourne,
            # balance_of_power=balance_of_power,
            # profession1=getattr(AltCustom, (next(iter(current_professions[0:1] or []), 'Missing')).upper()),
            profession1=next(iter(current_professions[0:1] or []), 0),
            # profession2=getattr(AltCustom, (next(iter(current_professions[1:2] or []), 'Missing')).upper()),
            profession2=next(iter(current_professions[1:2] or []), 0),
            lastRefresh=timezone.now(),
        )
    finally:
        pass
