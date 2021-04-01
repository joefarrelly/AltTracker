
import requests
#import environ

#env = environ.Env()
#environ.Env.read_env()

#BLIZZ_CLIENT=env("BLIZZ_CLIENT")
#BLIZZ_SECRET=env("BLIZZ_SECRET")

def getToken(BLIZZ_CLIENT,BLIZZ_SECRET):
	url = 'https://eu.battle.net/oauth/token?grant_type=client_credentials'
	myobj = {'client_id': BLIZZ_CLIENT, 'client_secret': BLIZZ_SECRET}
	x = requests.post(url, data = myobj)
	token = x.json()['access_token']
	return token

def getAuthAlts(authToken):
	url = "https://eu.api.blizzard.com/profile/user/wow?namespace=profile-eu&locale=en_US"
	myobj = {'access_token': authToken}
	y = requests.get(url, params = myobj)
	if y.status_code == 200:
		#Alt.objects.all().delete()
		#response = y.content
		#altData = []
		test = y.json()['wow_accounts'][0]['characters']
		for key in test:
			alt = key['id']
			level = key['level']
			name = key['name']
			realm = key['realm']['name']
			altClass = key['playable_class']['name']
			altRace = key['playable_race']['name']
			gender =  key['gender']['name']
			faction = key['faction']['name']
			nameSlug = name.lower()
			realmSlug = realm.lower()
			altClassSlug = altClass.lower()
			#tempAlt = AltClass(name,realm,altClass,nameSlug,realmSlug,altClassSlug)
			#tempAltForm = SaveAltsForm(tempAlt)
			if not Alt.objects.filter(altId=key['id']).exists():
				p = Alt.objects.create(altId=alt,altLevel=level,altName=name,altRealm=realm,altClass=altClass,altRace=altRace,altGender=gender,altFaction=faction)
			#altData.append(tempAlt)
	else:
		test = 'IT DIDNT WORK'
		return HttpResponse(test)
