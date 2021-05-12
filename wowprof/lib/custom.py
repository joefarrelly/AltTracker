import requests
import environ
import datetime
from django.utils import timezone
from wowprof.models import *

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


def getAuthAlts(authToken):
    url = "https://eu.api.blizzard.com/profile/user/wow?namespace=profile-eu&locale=en_US"
    myobj = {'access_token': authToken}
    y = requests.get(url, params=myobj)
    if y.status_code == 200:
        # Alt.objects.all().delete()
        # response = y.content
        # altData = []
        test = y.json()['wow_accounts'][0]['characters']
        for key in test:
            alt = key['id']
            level = key['level']
            name = key['name']
            realm = key['realm']['name']
            altClass = key['playable_class']['name']
            altRace = key['playable_race']['name']
            gender = key['gender']['name']
            faction = key['faction']['name']
            nameSlug = name.lower()
            realmSlug = realm.lower()
            altClassSlug = altClass.lower()
            # tempAlt = AltClass(name,realm,altClass,nameSlug,realmSlug,altClassSlug)
            # tempAltForm = SaveAltsForm(tempAlt)
            if not Alt.objects.filter(altId=key['id']).exists():
                p = Alt.objects.create(altId=alt, altLevel=level, altName=name, altRealm=realm, altClass=altClass, altRace=altRace, altGender=gender, altFaction=faction)
            # altData.append(tempAlt)
    else:
        test = 'IT DIDNT WORK'
        return HttpResponse(test)


def get_alt_data_temp(alts):
    for alt in alts:
        alt_obj = Alt.objects.get(altId=alt)
        getAltData(((alt_obj.altName).replace('\'', '')).lower(), (alt_obj.altRealm).lower(), alt_obj)


def getAltData(name, realm, alt_obj):
    print(name + '-' + realm)
    client_token = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
    params = {'access_token': client_token, 'namespace': 'profile-eu', 'locale': 'en_US'}
    urls = [
        'https://eu.api.blizzard.com/profile/wow/character/' + ((realm).replace('\'', '')).lower() + '/' + (name).lower() + '/professions',
        'https://eu.api.blizzard.com/profile/wow/character/' + ((realm).replace('\'', '')).lower() + '/' + (name).lower() + '/achievements',
        'https://eu.api.blizzard.com/profile/wow/character/' + ((realm).replace('\'', '')).lower() + '/' + (name).lower() + '/quests/completed',
        'https://eu.api.blizzard.com/profile/wow/character/' + ((realm).replace('\'', '')).lower() + '/' + (name).lower() + '/character-media'
    ]
    for url in urls:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            if 'professions' in url:
                # print('professions')
                try:
                    data = response.json()['primaries']
                    current_professions = []
                    for profession in data:
                        try:
                            obj = AltProfession.objects.get(alt=alt_obj, professionName=profession['profession']['name'])
                            obj.altProfessionExpiryDate = timezone.now() + datetime.timedelta(days=30)
                            obj.professionData = profession['tiers']
                            obj.save()
                        except AltProfession.DoesNotExist:
                            AltProfession.objects.create(
                                alt=alt_obj,
                                professionName=profession['profession']['name'],
                                altProfessionExpiryDate=timezone.now() + datetime.timedelta(days=30),
                                professionData=(profession['tiers'])
                            )
                        finally:
                            current_professions.append(profession['profession']['name'])
                    existing_professions = AltProfession.objects.filter(alt=alt_obj)
                    print(existing_professions)
                    for profession in existing_professions:
                        if not (profession.professionName in current_professions):
                            print('Delete the profession: ' + profession.professionName)
                            profession.delete()
                        else:
                            print('Do not delete the profession: ' + profession.professionName)
                except KeyError:
                    print(name + '-' + realm + ' has no professions data')
                    pass
            elif 'achievements' in url:
                # print('achievements')
                try:
                    data = response.json()['achievements']
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
                    pass
            elif 'quests/completed' in url:
                # print('quests')
                try:
                    data = response.json()['quests']
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
                    pass
            elif 'character-media' in url:
                # print('media')
                try:
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
                    pass
