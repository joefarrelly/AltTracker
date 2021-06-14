from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.http import FileResponse

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

import time

import datetime

import django_rq

import pandas as pd

env = environ.Env()
environ.Env.read_env()

BLIZZ_CLIENT = env("BLIZZ_CLIENT")
BLIZZ_SECRET = env("BLIZZ_SECRET")
# Create your views here.
HOST_IP = env("HOST_IP")
# LOCAL_IP="127.0.0.1:8000"

# MAIN_IP=LOCAL_IP
MAIN_IP = HOST_IP

alt_table_header = [
    "Faction",
    "Level",
    "Name",
    "Realm",
    "Class",
    "Profession 1",
    "Profession 2",
    "Item Level"
]

alt_checker_table_header = [
    "Faction",
    "Level",
    "Name",
    "Realm",
    "Class",
    "Mount Skill",
    "Garrison",
    "Mage Tower",
    "Shadowmourne",
    "Location",
    "Gold"
]

# def test_table(request):
#     # obj = your_model_name.objects.get(id=id)
#     # filename = obj.model_attribute_name.path
#     temp_csv = pd.read_html('https://fazztools.hopto.org/wowprof/alts')
#     # response = FileResponse(open('wowprof/admin.py', 'rb'))
#     # return response
#     return HttpResponse(temp_csv)


def wowProfHome(request):
    if request.method == 'POST':
        if 'alt-tracker-button' in request.POST:
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=fuzzywuzzyboo32&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)
    if request.method == 'GET':
        return render(request, "wowprof/wowprof_home.html")


def wowProfRedirect(request):
    code = request.GET.get('code')
    authToken = get_auth_token(BLIZZ_CLIENT, BLIZZ_SECRET, code)
    request.session['auth_token'] = authToken
    if request.GET.get('state') == 'blizzardeumz76c':
        print('looooooooooong')
        url = "https://eu.api.blizzard.com/profile/user/wow?namespace=profile-eu&locale=en_US"
        myobj = {'access_token': authToken}
        y = requests.get(url, params=myobj)
        if y.status_code == 200:
            altId = []
            test1 = y.json()['wow_accounts']
            for key1 in test1:
                test = key1['characters']
                for key in test:
                    altId.append(key['id'])
                    try:
                        obj = Alt.objects.get(altId=key['id'])
                        obj.altLevel = key['level']
                        obj.altName = key['name']
                        obj.altRealm = key['realm']['name']
                        obj.altRealmId = key['realm']['id']
                        obj.altRealmSlug = key['realm']['slug']
                        obj.altClass = key['playable_class']['id']
                        obj.altRace = key['playable_race']['id']
                        obj.altGender = key['gender']['name']
                        obj.altFaction = key['faction']['name']
                        obj.altExpiryDate = timezone.now() + datetime.timedelta(days=30)
                        obj.save()
                    except Alt.DoesNotExist:
                        Alt.objects.create(
                            altId=key['id'],
                            altLevel=key['level'],
                            altName=key['name'],
                            altRealm=key['realm']['name'],
                            altRealmId=key['realm']['id'],
                            altRealmSlug=key['realm']['slug'],
                            altClass=key['playable_class']['id'],
                            altRace=key['playable_race']['id'],
                            altGender=key['gender']['name'],
                            altFaction=key['faction']['name'],
                            altExpiryDate=timezone.now() + datetime.timedelta(days=30)
                        )
            request.session['altId'] = altId
    else:
        print('not long')
        # print(request.session.session_key)
    return redirect("/wowprof/alts/")


def wowProfAlts(request):
    if request.method == 'POST':
        if 'login-button' in request.POST:
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=blizzardeumz76c&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)
        if 'alt-tracker-home-button' in request.POST:
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=fuzzywuzzyboo32&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)
        if 'logout-button' in request.POST:
            request.session['altId'] = []
            request.session['auth_token'] = ''
            return render(request, "wowprof/wowprof_alts.html")
    if request.method == 'GET':
        alt_objects = []
        if 'altId' in request.session:
            alt_objects = Alt.objects.select_related('altcustom').filter(pk__in=request.session['altId']).order_by('-altLevel', '-altcustom__average_item_level')
        if request.GET:
            if request.GET['format'] == 'csv':
                csv_export = []
                for alt in alt_objects:
                    csv_export.append([alt.altFaction, alt.altLevel, alt.altName, alt.altRealm, alt.get_altClass_display(), alt.altcustom.get_profession1_display(), alt.altcustom.get_profession2_display(), alt.altcustom.average_item_level])
                alt_df = pd.DataFrame(csv_export, index=list(range(1, len(csv_export) + 1)), columns=alt_table_header)
                response = HttpResponse(alt_df.to_csv(index_label='Index'))
                response['Content-Disposition'] = 'attachment; filename=alt_data.csv'
                return response
        return render(request, "wowprof/wowprof_alts.html", {'altData': alt_objects})


def refresh_character(request):
    name, realm = request.GET.get('name'), request.GET.get('realm')
    # print(request.session['auth_token'])
    alt_obj = Alt.objects.get(altName=name, altRealm=realm)
    job = django_rq.enqueue(getAltData, (name.replace('\'', '')).lower(), (realm.replace('\'', '')).lower(), alt_obj, request.session['auth_token'])
    while not job.result:
        time.sleep(3)
    alt_obj, custom_obj = job.result
    prof1_href = prof2_href = ''
    if custom_obj.profession1 != 0:
        prof1_href = (name.replace('\'', '')).lower() + "/" + (realm.replace('\'', '')).lower() + "/profession/" + (custom_obj.get_profession1_display()).lower()
    if custom_obj.profession2 != 0:
        prof2_href = (name.replace('\'', '')).lower() + "/" + (realm.replace('\'', '')).lower() + "/profession/" + (custom_obj.get_profession2_display()).lower()
    context = {
        "last_updated": date_diff_format(custom_obj.lastRefresh),
        "gear": int(custom_obj.average_item_level),
        "prof1": custom_obj.get_profession1_display(),
        "prof2": custom_obj.get_profession2_display(),
        "prof1_href": prof1_href,
        "prof2_href": prof2_href,
        "level": alt_obj.altLevel
    }
    data = json.dumps(context)
    return HttpResponse(data, content_type='application/json')


def wowProfAltsProfession(request, name, realm, profession):
    alt_obj = get_object_or_404(Alt, altName=name.capitalize(), altRealmSlug=realm)
    profession_obj = get_object_or_404(AltProfession, alt=alt_obj, profession=getattr(AltProfession.Profession, profession.upper()))
    return render(request, "wowprof/wowprof_alts_profession.html", {'alt': alt_obj, 'profession': profession_obj})


def wowProfAltsMoreDetails(request, name, realm):
    try:
        alt_obj = Alt.objects.get(altName=name.capitalize(), altRealmSlug=realm)
    except Alt.DoesNotExist:
        alt_obj = 0
    try:
        media_obj = AltMedia.objects.get(alt=alt_obj)
    except AltMedia.DoesNotExist:
        media_obj = []
    try:
        equipment_objs = AltEquipment.objects.prefetch_related('equipment').filter(alt=alt_obj)
        filtered_equipment_objs = {}
        for item in equipment_objs:
            filtered_equipment_objs[item.slot] = item
    except AltEquipment.DoesNotExist:
        filtered_equipment_objs = {}
    return render(request, "wowprof/wowprof_alts_more.html", {'alt': alt_obj, 'media': media_obj, 'equipment': filtered_equipment_objs})


def wowProfChecker(request):
    if request.method == 'POST':
        if 'alt-tracker-home-button-checker' in request.POST:
            url = 'https://eu.battle.net/oauth/authorize?client_id=' + BLIZZ_CLIENT + '&scope=wow.profile&state=fuzzywuzzyboo32&redirect_uri=http%3A%2F%2F' + MAIN_IP + '%2Fwowprof%2Fredirect%2F&response_type=code'
            return redirect(url)
    if request.method == 'GET':
        alt_objects = []
        if 'altId' in request.session:
            alt_objects = Alt.objects.select_related('altcustom').filter(pk__in=request.session['altId']).order_by('-altLevel', '-altcustom__average_item_level')
        if request.GET:
            if request.GET['format'] == 'csv':
                csv_export = []
                for alt in alt_objects:
                    csv_export.append([alt.altFaction, alt.altLevel, alt.altName, alt.altRealm, alt.get_altClass_display(), alt.altcustom.get_mount_display(), alt.altcustom.get_garrison_display(), alt.altcustom.get_mageTower_display(), alt.altcustom.get_shadowmourne_display(), alt.altcustom.location, alt.altcustom.gold])
                alt_df = pd.DataFrame(csv_export, index=list(range(1, len(csv_export) + 1)), columns=alt_checker_table_header)
                response = HttpResponse(alt_df.to_csv(index_label='Index'))
                response['Content-Disposition'] = 'attachment; filename=alt_checker_data.csv'
                return response
        return render(request, 'wowprof/wowprof_checker.html', {'altData': alt_objects})


def wowProfRequiem(request):
    pass
#     if request.method == 'POST':
#         if 'wowprof-requiem-refresh-button' in request.POST:
#             Requiem.objects.all().delete()
#             clientToken = getToken(BLIZZ_CLIENT, BLIZZ_SECRET)
#             anObj = {'access_token': clientToken, 'namespace': 'profile-eu', 'locale': 'en_US'}
#             url = 'https://eu.api.blizzard.com/data/wow/guild/doomhammer/requiem/roster'
#             y = requests.get(url, params=anObj)
#             if y.status_code == 200:
#                 reqData = y.json()['members']
#                 for key in reqData:
#                     if (key['rank'] == 0) or (key['rank'] == 1) or (key['rank'] == 4) or (key['rank'] == 5) or (key['rank'] == 6):
#                         reqId = key['character']['id']
#                         # reqLevel=key['character']['level']
#                         reqName = key['character']['name']
#                         tempReqRealm = key['character']['realm']['slug']
#                         reqRealm = tempReqRealm.capitalize()
#                         # reqClass=key['character']['playable_class']['id']
#                         reqRank = key['rank']
#                         url = 'https://eu.api.blizzard.com/profile/wow/character/' + tempReqRealm + '/' + reqName.lower()
#                         x = requests.get(url, params=anObj)
#                         if x.status_code == 200:
#                             reqAltData = x.json()
#                             if Alt.objects.filter(altId=reqId).exists():
#                                 q = get_object_or_404(Alt, altId=reqId)
#                                 q.altLevel = reqAltData['level']
#                                 q.altName = reqAltData['name']
#                                 q.altRealm = reqAltData['realm']['name']
#                                 q.altClass = reqAltData['character_class']['name']
#                                 q.altRace = reqAltData['race']['name']
#                                 q.altGender = reqAltData['gender']['name']
#                                 q.altFaction = reqAltData['faction']['name']
#                                 q.altExpiryDate = timezone.now() + datetime.timedelta(days=30)
#                                 q.save()
#                             else:       # Alt.objects.filter(altId=key['id']).exists():
#                                 p = Alt.objects.create(
#                                     altId=reqId,
#                                     altLevel=reqAltData['level'],
#                                     altName=reqAltData['name'],
#                                     altRealm=reqAltData['realm']['name'],
#                                     altClass=reqAltData['character_class']['name'],
#                                     altRace=reqAltData['race']['name'],
#                                     altGender=reqAltData['gender']['name'],
#                                     altFaction=reqAltData['faction']['name'],
#                                     altExpiryDate=timezone.now() + datetime.timedelta(days=30),
#                                 )
#                             tempReqAlt = get_object_or_404(Alt, altId=reqId)
#                             if Requiem.objects.filter(alt=tempReqAlt).exists():
#                                 q = get_object_or_404(Requiem, alt=reqId)
#                                 # q.reqLevel=reqLevel
#                                 q.reqName = reqName
#                                 q.reqRealm = reqRealm
#                                 # q.reqClass=reqClass
#                                 q.reqRank = reqRank
#                                 q.reqExpiryDate = timezone.now() + datetime.timedelta(days=30)
#                                 q.save()
#                             else:       # Alt.objects.filter(altId=key['id']).exists():
#                                 p = Requiem.objects.create(
#                                     alt=tempReqAlt,
#                                     # reqLevel=reqLevel,
#                                     reqName=reqName,
#                                     reqRealm=reqRealm,
#                                     # reqClass=reqClass,
#                                     reqRank=reqRank,
#                                     reqExpiryDate=timezone.now() + datetime.timedelta(days=30)
#                                 )
#                             print(reqName)
#     altData = []
#     reqAlts = Requiem.objects.all()
#     for alt in reqAlts:
#         tempInstance = get_object_or_404(Alt, altId=alt.alt_id)
#         # tempInstance=Alt.objects.filter(altId=alt)
#         rank = alt.reqRank
#         name = tempInstance.altName
#         nameSlug = name.lower()
#         realm = tempInstance.altRealm
#         realmSlug = realm.lower()
#         altClass = tempInstance.altClass
#         clothRank = leatherRank = mailRank = plateRank = miscRank = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
#         profession1 = profession1Data = profession2 = profession2Data = 'Missing'
#         # profession2='Missing'
#         if AltProfession.objects.filter(alt=tempInstance).exists():
#             tempProf = AltProfession.objects.filter(alt=tempInstance)
#             # if tempProf.count() == 1:
#             profession1 = tempProf[0].professionName
#             profession1Data = tempProf[0].professionData
#             # print(profession1Data)
#             # profession1Slug=profession1.lower()
#             if tempProf.count() > 1:
#                 profession2 = tempProf[1].professionName
#                 profession2Data = tempProf[1].professionData
#                 # profession2Slug=profession2.lower()

#             # else:
#             #   profession1=tempProf[0].professionName
#             #   profession2=tempProf[1].professionName

#         # for prof in profession1Data:

#         # for prof in profession2Data:

#         tempAlt = ReqAltClass(name, realm, altClass, rank, clothRank, leatherRank, mailRank, plateRank, miscRank, profession1, profession2)
#         altData.append(tempAlt)
#     # tempMyObj={'name':'name'}
#     return render(request, "wowprof/wowprof_requiem.html", {'altData': altData})
