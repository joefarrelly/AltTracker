from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.shortcuts import get_object_or_404

from django.utils import timezone

from wowprof.lib.classes import *
from wowprof.lib.custom import *
from wowprof.models import *

from .forms import *

# import lxml.html
from bs4 import BeautifulSoup

import environ
import requests
import json

import datetime

import django_rq

env = environ.Env()
environ.Env.read_env()

BLIZZ_CLIENT = env("BLIZZ_CLIENT")
BLIZZ_SECRET = env("BLIZZ_SECRET")
# Create your views here.
HOST_IP = env("HOST_IP")
# LOCAL_IP="127.0.0.1:8000"

# MAIN_IP=LOCAL_IP
MAIN_IP = HOST_IP


# altData = []
# def index(request):
#   return render(
#       request,
#       "home/home.html")

# def index(request):
#   return HttpResponse(env("BLIZZ_SECRET")+"  :  "+env("BLIZZ_CLIENT"))

def wowProfHome(request):
    if request.method == 'POST':
        if ('wowprof-home-delete-button' in request.POST):
            tempDel = 112997951
        # Alt.objects.filter(altId=tempDel).delete()
            Alt.objects.all().delete()
        else:
            # url = 'https://us.battle.net/oauth/token?grant_type=client_credentials'
            # myobj = {'client_id': BLIZZ_CLIENT, 'client_secret': BLIZZ_SECRET}
            # x = requests.post(url, data = myobj)
            # token = x.json()['access_token']
            # return HttpResponse("it worked" + token)
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=blizzardeumz76c&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)
    if 'code' in request.session:
        temp2 = {
            'code': request.session['code'],
            'state': request.session['state'],
        }
    else:
        temp2 = {
            'code': 'N/A',
            'state': 'N/A',
        }
    return render(request, "wowprof/wowprof_home.html", temp2)


def wowProfRedirect(request):
    code = request.GET.get('code')
    state = request.GET.get('state')

    request.session['code'] = code
    request.session['state'] = state
    tempUri = 'http://' + MAIN_IP + '/wowprof/redirect/'
    url = 'https://eu.battle.net/oauth/token?grant_type=authorization_code'
    myobj = {'client_id': BLIZZ_CLIENT, 'client_secret': BLIZZ_SECRET, 'code': code, 'redirect_uri': tempUri}
    x = requests.post(url, data=myobj)
    authToken = x.json()['access_token']

    request.session['authToken'] = authToken

    # altList = ['1','2']

    # temp = {
    #   'code':code,
    #   'state':state,
    # }

    url = "https://eu.api.blizzard.com/profile/user/wow?namespace=profile-eu&locale=en_US"
    myobj = {'access_token': authToken}
    y = requests.get(url, params=myobj)
    if y.status_code == 200:
        # Alt.objects.all().delete()
        # response = y.content
        # altData = []
        altId = []
        # test = y.json()['wow_accounts'][0]['characters']
        test1 = y.json()['wow_accounts']
        for key1 in test1:
            test = key1['characters']
            for key in test:
                # alt = key['id']
                # level = key['level']
                name = key['name']
                realm = key['realm']['name']
                altClass = key['playable_class']['name']
                # altRace = key['playable_race']['name']
                # gender =  key['gender']['name']
                # faction = key['faction']['name']
                nameSlug = name.lower()
                realmSlug = realm.lower()
                altClassSlug = altClass.lower()
                # tempAlt = AltClass(name,realm,altClass,nameSlug,realmSlug,altClassSlug)
                # tempAltForm = SaveAltsForm(tempAlt)
                altId.append(key['id'])
                if Alt.objects.filter(altId=key['id']).exists():
                    q = get_object_or_404(Alt, altId=key['id'])
                    q.altLevel = key['level']
                    q.altName = key['name']
                    q.altRealm = key['realm']['name']
                    q.altClass = key['playable_class']['name']
                    q.altRace = key['playable_race']['name']
                    q.altGender = key['gender']['name']
                    q.altFaction = key['faction']['name']
                    q.altExpiryDate = timezone.now() + datetime.timedelta(days=30)
                    q.save()
                else:       # Alt.objects.filter(altId=key['id']).exists():
                    p = Alt.objects.create(
                        altId=key['id'],
                        altLevel=key['level'],
                        altName=key['name'],
                        altRealm=key['realm']['name'],
                        altClass=key['playable_class']['name'],
                        altRace=key['playable_race']['name'],
                        altGender=key['gender']['name'],
                        altFaction=key['faction']['name'],
                        altExpiryDate=timezone.now() + datetime.timedelta(days=30),
                    )
                # altData.append(tempAlt)
        request.session['altId'] = altId
    else:
        test = 'IT DIDNT WORK'
        return HttpResponse(test)

    return redirect("/wowprof/alts/")


def wowProfAlts(request):
    if request.method == 'POST':
        if 'wowprof-alts-refresh-button' in request.POST:
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=blizzardeumz76c&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)

        if 'wowprof-alts-refresh-data-button' in request.POST:
            if 'altId' in request.session:
                django_rq.enqueue(get_alt_data_temp, request.session['altId'])

        if 'wowprof-alts-scan-professions-button' in request.POST:
            foo = ['1', '2']
            baz = ['apple']
            django_rq.enqueue(my_func, foo, bar=baz)
        #     print("One")
        #     temptemp = []
        #     clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
        #     anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
        #     j = Alt.objects.all()
        #     for i in j:
        #         print("Two")
        #         name = i.altName
        #         tempRealm = i.altRealm
        #         realm = tempRealm.replace('\'', '')
        #         url = 'https://eu.api.blizzard.com/profile/wow/character/' + realm.lower() + '/' + name.lower() + '/professions'
        #         y = requests.get(url, params=anObj)
        #         if y.status_code == 200:
        #             profData = y.json()
        #             AltProfession.objects.filter(alt=i).delete()
        #             print(AltProfession.objects.filter(alt=i))
        #             if 'primaries' in profData:
        #                 # temptemp.append("YES")
        #                 test3 = y.json()['primaries']
        #                 for key in test3:
        #                     print("Three")
        #                     professionName = key['profession']['name']
        #                     # testThing = altData
        #                     # return HttpResponse(testThing)
        #                     # if not AltProfession.objects.filter(alt=i,professionName=professionName).exists():
        #                     p = AltProfession.objects.create(
        #                         alt=i,
        #                         professionName=professionName,
        #                         altProfessionExpiryDate=timezone.now() + datetime.timedelta(days=30),
        #                         professionData=(key['tiers'])
        #                     )
        #                 print(AltProfession.objects.filter(alt=i))
        # if 'wowprof-alts-scan-achievements-button' in request.POST:
        #     clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
        #     anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
        #     # page=requests.get("http://127.0.0.1:8000/wowprof/alts/")
        #     if 'altId' in request.session:
        #         for alt in request.session['altId']:
        #             tempInstance = get_object_or_404(Alt, altId=alt)
        #             name = tempInstance.altName
        #             # nameSlug=name.lower()
        #             tempRealm = tempInstance.altRealm
        #             realm = tempRealm.replace('\'', '')
        #             # realmSlug=realm.lower()
        #             url = 'https://eu.api.blizzard.com/profile/wow/character/' + realm.lower() + '/' + name.lower() + '/achievements'
        #             y = requests.get(url, params=anObj)
        #             if y.status_code == 200:
        #                 achData = y.json()
        #                 if AltAchievement.objects.filter(alt=tempInstance).exists():
        #                     q = get_object_or_404(AltAchievement, alt=tempInstance)
        #                     q.achievementData = achData['achievements']
        #                     q.altAchievementExpiryDate = timezone.now() + datetime.timedelta(days=30)
        #                     q.save()
        #                 else:
        #                     a = AltAchievement.objects.create(
        #                         alt=tempInstance,
        #                         achievementData=achData['achievements'],
        #                         altAchievementExpiryDate=timezone.now() + datetime.timedelta(days=30),
        #                     )
        #                 print(tempInstance.altName)
        #             else:
        #                 print(alt)
        # if 'wowprof-alts-scan-quest-completed-button' in request.POST:
        #     clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
        #     anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
        #     if 'altId' in request.session:
        #         for alt in request.session['altId']:
        #             tempInstance = get_object_or_404(Alt, altId=alt)
        #             name = tempInstance.altName
        #             tempRealm = tempInstance.altRealm
        #             realm = tempRealm.replace('\'', '')
        #             url = 'https://eu.api.blizzard.com/profile/wow/character/' + realm.lower() + '/' + name.lower() + '/quests/completed'
        #             y = requests.get(url, params=anObj)
        #             if y.status_code == 200:
        #                 questData = y.json()
        #                 if AltQuestCompleted.objects.filter(alt=tempInstance).exists():
        #                     q = get_object_or_404(AltQuestCompleted, alt=tempInstance)
        #                     q.questCompletedData = questData['quests']
        #                     q.altQuestCompletedExpiryDate = timezone.now() + datetime.timedelta(days=30)
        #                     q.save()
        #                 else:
        #                     a = AltQuestCompleted.objects.create(
        #                         alt=tempInstance,
        #                         questCompletedData=questData['quests'],
        #                         altQuestCompletedExpiryDate=timezone.now() + datetime.timedelta(days=30),
        #                     )
        #                 print(tempInstance.altName)
        #             # print(y.json())
        #     # return render(request, "wowprof/wowprof_alts.html")
        #         # temptemp.append(name)
        #         # temptemp.append(realm)
        #         # temptemp.append(y.status_code)
        #     # return HttpResponse(temptemp)
        # if 'wowprof-alts-scan-media-button' in request.POST:
        #     clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
        #     anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
        #     if 'altId' in request.session:
        #         for alt in request.session['altId']:
        #             tempInstance = get_object_or_404(Alt, altId=alt)
        #             name = tempInstance.altName
        #             tempRealm = tempInstance.altRealm
        #             realm = tempRealm.replace('\'', '')
        #             url = 'https://eu.api.blizzard.com/profile/wow/character/' + realm.lower() + '/' + name.lower() + '/character-media'
        #             y = requests.get(url, params=anObj)
        #             if y.status_code == 200:
        #                 if 'assets' in y.json():
        #                     mediaData = y.json()['assets']
        #                     # print(mediaData)
        #                     # mediaJSON=json.loads(mediaData)
        #                     # print(mediaJSON)
        #                     for i in mediaData:
        #                         if i['key'] == 'avatar':
        #                             avatar = i['value']
        #                         elif i['key'] == 'inset':
        #                             inset = i['value']
        #                         elif i['key'] == 'main':
        #                             main = i['value']
        #                         elif i['key'] == 'main-raw':
        #                             mainRaw = i['value']
        #                     print(avatar)
        #                     print(inset)
        #                     print(main)
        #                     print(mainRaw)
        #                     # for med in mediaData:
        #                     #   print(med)
        #                 if AltMedia.objects.filter(alt=tempInstance).exists():
        #                     m = get_object_or_404(AltMedia, alt=tempInstance)
        #                     m.avatar = avatar
        #                     m.inset = inset
        #                     m.main = main
        #                     m.mainRaw = mainRaw
        #                     m.altMediaExpiryDate = timezone.now() + datetime.timedelta(days=30)
        #                     m.save()
        #                 else:
        #                     a = AltMedia.objects.create(
        #                         alt=tempInstance,
        #                         avatar=avatar,
        #                         inset=inset,
        #                         main=main,
        #                         mainRaw=mainRaw,
        #                         altMediaExpiryDate=timezone.now() + datetime.timedelta(days=30),
        #                     )
        #                 print(tempInstance.altName)

    altData = []
    allAlts = Alt.objects.all()
    altProf = AltProfession.objects.all()
    if 'altId' in request.session:
        # if request.session.has_key('altId'):
        for alt in request.session['altId']:
            tempInstance = get_object_or_404(Alt, altId=alt)
            # tempInstance=Alt.objects.filter(altId=alt)
            faction = tempInstance.altFaction
            level = tempInstance.altLevel
            name = tempInstance.altName
            nameSlug = name.lower()
            realm = tempInstance.altRealm
            tempRealmSlug = realm.lower()
            realmSlug = tempRealmSlug.replace('\'', '')
            altClass = tempInstance.altClass
            # mount=garrison='N/A'
            mount = garrison = mt = 0
            if AltAchievement.objects.filter(alt=alt).exists():
                tempAch = AltAchievement.objects.filter(alt=alt)
                tempAchData = tempAch[0].achievementData
                testing12 = tempAchData[0]
                for key in tempAch[0].achievementData:
                    testing12 = key['id']
                    # testing34=key['criteria']
                    if testing12 == 891 and key['criteria']['is_completed']:
                        # testing34=key['criteria']['is_completed']
                        # if testing34 == True:
                        # mount='1- Slow Mount'
                        mount += 1
                    elif testing12 == 889 and key['criteria']['is_completed']:
                        # mount='2- Fast Mount'
                        mount += 1
                    elif testing12 == 890 and key['criteria']['is_completed']:
                        # mount='3- Slow Flying'
                        mount += 1
                    elif testing12 == 5180 and key['criteria']['is_completed']:
                        # mount='4- Fast Flying'
                        mount += 1
                    elif testing12 == 9100 and key['criteria']['is_completed']:
                        # garrison='Level 2'
                        garrison += 1
                    elif testing12 == 9101 and key['criteria']['is_completed']:
                        # garrison='Level 3'
                        garrison += 1
                    elif testing12 == 9545 and key['criteria']['is_completed']:
                        garrison += 1
                    elif testing12 == 9546 and key['criteria']['is_completed']:
                        garrison += 1
                # print(testing12)
            profession1 = profession1Slug = profession2 = profession2Slug = 'Missing'
            # profession2='Missing'
            if AltProfession.objects.filter(alt=alt).exists():
                tempProf = AltProfession.objects.filter(alt=alt)
                # if tempProf.count() == 1:
                profession1 = tempProf[0].professionName
                profession1Slug = profession1.lower()
                if tempProf.count() > 1:
                    profession2 = tempProf[1].professionName
                    profession2Slug = profession2.lower()

                # else:
                #   profession1=tempProf[0].professionName
                #   profession2=tempProf[1].professionName
            if AltQuestCompleted.objects.filter(alt=alt).exists():
                tempQuest = AltQuestCompleted.objects.filter(alt=alt)
                for key in tempQuest[0].questCompletedData:
                    testing56 = key['id']
                    if testing56 == 36848:
                        mt += 1
            tempAlt = AltClass(faction, level, name, nameSlug, realm, realmSlug, altClass, mount, garrison, mt, profession1, profession1Slug, profession2, profession2Slug)
            altData.append(tempAlt)
        # print(testing12)

    # for key, value in request.session.items():
    #   print(key, value)

    # code = request.session['code']
    # state = request.session['state']
    # authToken = request.session['authToken']
    # tempUri = 'http://'+MAIN_IP+'/wowprof/redirect/'
    # tempScope = 'wow.profile'

    # altList = altList

    # url = 'https://eu.battle.net/oauth/token?grant_type=authorization_code'
    # myobj = {'client_id': BLIZZ_CLIENT, 'client_secret': BLIZZ_SECRET, 'code':code, 'redirect_uri':tempUri}
    # x = requests.post(url, data = myobj)
    # token = x.json()['access_token']

    # getAuthAlts(authToken)
    # url = "https://eu.api.blizzard.com/profile/user/wow?namespace=profile-eu&locale=en_US"
    # myobj = {'access_token': authToken}
    # y = requests.get(url, params = myobj)
    # if y.status_code == 200:
    #   #Alt.objects.all().delete()
    #   #response = y.content
    #   altData = []
    #   test = y.json()['wow_accounts'][0]['characters']
    #   for key in test:
    #       #alt = key['id']
    #       #level = key['level']
    #       name = key['name']
    #       realm = key['realm']['name']
    #       altClass = key['playable_class']['name']
    #       #altRace = key['playable_race']['name']
    #       #gender =  key['gender']['name']
    #       #faction = key['faction']['name']
    #       nameSlug = name.lower()
    #       realmSlug = realm.lower()
    #       altClassSlug = altClass.lower()
    #       tempAlt = AltClass(name,realm,altClass,nameSlug,realmSlug,altClassSlug)
    #       #tempAltForm = SaveAltsForm(tempAlt)
    #       if Alt.objects.filter(altId=key['id']).exists():
    #           q = get_object_or_404(Alt,altId=key['id'])
    #           q.altLevel=key['level']
    #           q.altName=key['name']
    #           q.altRealm=key['realm']['name']
    #           q.altClass=key['playable_class']['name']
    #           q.altRace=key['playable_race']['name']
    #           q.altGender=key['gender']['name']
    #           q.altFaction=key['faction']['name']
    #           q.save()
    #       else:       #Alt.objects.filter(altId=key['id']).exists():
    #           p = Alt.objects.create(
    #               altId=key['id'],
    #               altLevel=key['level'],
    #               altName=key['name'],
    #               altRealm=key['realm']['name'],
    #               altClass=key['playable_class']['name'],
    #               altRace=key['playable_race']['name'],
    #               altGender=key['gender']['name'],
    #               altFaction=key['faction']['name']
    #           )
    #       altData.append(tempAlt)
    # else:
    #   test = 'IT DIDNT WORK'
    #   return HttpResponse(test)
    # request.session['altData'] = altData
    return render(request, "wowprof/wowprof_alts.html", {'altData': altData})  # 'code':code,'state':state


def wowProfAltsProfession(request, name, realm, profession):
    # myobj = {'name':name,'realm':realm,'profession':profession}
    # clientToken=getToken(BLIZZ_CLIENT,BLIZZ_SECRET)
    # anObj={'access_token':clientToken,'namespace':'profile-eu','locale':'en_US'}
    # url='https://eu.api.blizzard.com/profile/wow/character/'+realm.lower()+'/'+name.lower()+'/professions'
    # y = requests.get(url, params = anObj)
    # if y.status_code == 200:
    #   y.json()
    tempInstance = get_object_or_404(Alt, altName=name, altRealm=realm)
    tempAlt = tempInstance.altId
    tempInstance2 = get_object_or_404(AltProfession, alt=tempAlt, professionName=profession)
    # tempInstance=get_object_or_404(Alt, altId=alt)
    tempMyObj = tempInstance2.professionData
    # for key in tempMyObj:
    #   tempName=key['tier']['name']
    #   tempRecipe
    return render(request, "wowprof/wowprof_alts_profession.html", {'data': tempMyObj})


def wowProfAltsMoreDetails(request, name, realm):
    tempInstance = get_object_or_404(Alt, altName=name, altRealm=realm)
    tempAlt = tempInstance.altId
    tempInstance2 = get_object_or_404(AltMedia, alt=tempAlt)
    # tempData = tempInstance2.main
    tempData = tempInstance2.mainRaw
    return render(request, "wowprof/wowprof_alts_more.html", {'data': tempData})
# def calcHome(request):
#   return render(
#       request,
#       "wowprof/calc_home.html")


def wowProfRequiem(request):
    if request.method == 'POST':
        if 'wowprof-requiem-refresh-button' in request.POST:
            Requiem.objects.all().delete()
            clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
            anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
            url = 'https://eu.api.blizzard.com/data/wow/guild/doomhammer/requiem/roster'
            y = requests.get(url, params=anObj)
            if y.status_code == 200:
                reqData = y.json()['members']
                for key in reqData:
                    if (key['rank'] == 0) or (key['rank'] == 1) or (key['rank'] == 4) or (key['rank'] == 5) or (key['rank'] == 6):
                        reqId = key['character']['id']
                        # reqLevel=key['character']['level']
                        reqName = key['character']['name']
                        tempReqRealm = key['character']['realm']['slug']
                        reqRealm = tempReqRealm.capitalize()
                        # reqClass=key['character']['playable_class']['id']
                        reqRank = key['rank']
                        url = 'https://eu.api.blizzard.com/profile/wow/character/' + tempReqRealm + '/' + reqName.lower()
                        x = requests.get(url, params=anObj)
                        if x.status_code == 200:
                            reqAltData = x.json()
                            if Alt.objects.filter(altId=reqId).exists():
                                q = get_object_or_404(Alt, altId=reqId)
                                q.altLevel = reqAltData['level']
                                q.altName = reqAltData['name']
                                q.altRealm = reqAltData['realm']['name']
                                q.altClass = reqAltData['character_class']['name']
                                q.altRace = reqAltData['race']['name']
                                q.altGender = reqAltData['gender']['name']
                                q.altFaction = reqAltData['faction']['name']
                                q.altExpiryDate = timezone.now() + datetime.timedelta(days=30)
                                q.save()
                            else:       # Alt.objects.filter(altId=key['id']).exists():
                                p = Alt.objects.create(
                                    altId=reqId,
                                    altLevel=reqAltData['level'],
                                    altName=reqAltData['name'],
                                    altRealm=reqAltData['realm']['name'],
                                    altClass=reqAltData['character_class']['name'],
                                    altRace=reqAltData['race']['name'],
                                    altGender=reqAltData['gender']['name'],
                                    altFaction=reqAltData['faction']['name'],
                                    altExpiryDate=timezone.now() + datetime.timedelta(days=30),
                                )
                            tempReqAlt = get_object_or_404(Alt, altId=reqId)
                            if Requiem.objects.filter(alt=tempReqAlt).exists():
                                q = get_object_or_404(Requiem, alt=reqId)
                                # q.reqLevel=reqLevel
                                q.reqName = reqName
                                q.reqRealm = reqRealm
                                # q.reqClass=reqClass
                                q.reqRank = reqRank
                                q.reqExpiryDate = timezone.now() + datetime.timedelta(days=30)
                                q.save()
                            else:       # Alt.objects.filter(altId=key['id']).exists():
                                p = Requiem.objects.create(
                                    alt=tempReqAlt,
                                    # reqLevel=reqLevel,
                                    reqName=reqName,
                                    reqRealm=reqRealm,
                                    # reqClass=reqClass,
                                    reqRank=reqRank,
                                    reqExpiryDate=timezone.now() + datetime.timedelta(days=30)
                                )
                            print(reqName)
    altData = []
    reqAlts = Requiem.objects.all()
    for alt in reqAlts:
        tempInstance = get_object_or_404(Alt, altId=alt.alt_id)
        # tempInstance=Alt.objects.filter(altId=alt)
        rank = alt.reqRank
        name = tempInstance.altName
        nameSlug = name.lower()
        realm = tempInstance.altRealm
        realmSlug = realm.lower()
        altClass = tempInstance.altClass
        clothRank = leatherRank = mailRank = plateRank = miscRank = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
        profession1 = profession1Data = profession2 = profession2Data = 'Missing'
        # profession2='Missing'
        if AltProfession.objects.filter(alt=tempInstance).exists():
            tempProf = AltProfession.objects.filter(alt=tempInstance)
            # if tempProf.count() == 1:
            profession1 = tempProf[0].professionName
            profession1Data = tempProf[0].professionData
            # print(profession1Data)
            # profession1Slug=profession1.lower()
            if tempProf.count() > 1:
                profession2 = tempProf[1].professionName
                profession2Data = tempProf[1].professionData
                # profession2Slug=profession2.lower()

            # else:
            #   profession1=tempProf[0].professionName
            #   profession2=tempProf[1].professionName

        # for prof in profession1Data:

        # for prof in profession2Data:

        tempAlt = ReqAltClass(name, realm, altClass, rank, clothRank, leatherRank, mailRank, plateRank, miscRank, profession1, profession2)
        altData.append(tempAlt)
    # tempMyObj={'name':'name'}
    return render(request, "wowprof/wowprof_requiem.html", {'altData': altData})
