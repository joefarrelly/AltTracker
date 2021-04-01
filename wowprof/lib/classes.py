
class AltClass(object):
	def __init__(self,faction,level,name,nameSlug,realm,realmSlug,altClass,mount,garrison,mt,altProfession1=None,altProfession1Slug=None,altProfession2=None,altProfession2Slug=None): 
		DEFAULT_PROF='Missing'
		#self.alt=alt
		self.faction=faction
		self.level=level
		self.name=name
		self.realm=realm
		self.altClass=altClass
		self.mount=mount
		self.garrison=garrison
		self.mt=mt
		self.altProfession1=altProfession1 if altProfession1 is not None else DEFAULT_PROF
		self.altProfession2=altProfession2 if altProfession2 is not None else DEFAULT_PROF
		self.nameSlug=nameSlug
		self.realmSlug=realmSlug
		self.altProfession1Slug=altProfession1Slug if altProfession1Slug is not None else DEFAULT_PROF
		self.altProfession2Slug=altProfession2Slug if altProfession2Slug is not None else DEFAULT_PROF
		#self.nameSlug = nameSlug
		#self.realmSlug = realmSlug
		#self.altClassSlug = altClassSlug
		#self.altRace = altRace
		#if altProfession1 is None:
		#	altProfession1 = []
		# self.altProfession1 = altProfession1 if altProfession1 is not None else DEFAULT_PROF
		#if altProfession1Slug is None:
		#	altProfession1Slug = []
		# self.altProfession1Slug = altProfession1Slug if altProfession1Slug is not None #else DEFAULT_PROF
		#if altProfession2 is None:
		#	altProfession2 = []
		# self.altProfession2 = altProfession2 if altProfession2 is not None else DEFAULT_PROF
		#if altProfession2Slug is None:
		#	altProfession2Slug = []
		# self.altProfession2Slug = altProfession2Slug if altProfession2Slug is not None #else DEFAULT_PROF
# class AltClassSlug(object):
# 	def __init__(self,nameSlug,realmSlug,altProfession1Slug=None,altProfession2Slug=None):
# 		DEFAULT_PROF = 'Missing'
# 		self.nameSlug=nameSlug
# 		self.realmSlug=realmSlug
# 		self.altProfession1Slug=altProfession1Slug
# 		self.altProfession2Slug=altProfession2Slug

class ReqAltClass(object):
	def __init__(self,name,realm,altClass,rank,clothRank,leatherRank,mailRank,plateRank,miscRank,altProfession1=None,altProfession2=None): 
		DEFAULT_PROF='Missing'
		DEFAULT_RANK=['N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A','N/A']
		self.name=name
		self.realm=realm
		self.altClass=altClass
		self.rank=rank
		self.clothRank=clothRank
		self.leatherRank=leatherRank
		self.mailRank=mailRank
		self.plateRank=plateRank
		self.miscRank=miscRank
		self.altProfession1=altProfession1 if altProfession1 is not None else DEFAULT_PROF
		# self.altProfession1Data=altProfession1Data if altProfession1Data is not None else DEFAULT_PROF
		self.altProfession2=altProfession2 if altProfession2 is not None else DEFAULT_PROF
		# self.altProfession2Data=altProfession2Data if altProfession2Data is not None else DEFAULT_PROF

class AltProf:
	def __init__(self,alt,profession1,profession2):
		self.alt = alt
		self.profession1 = profession1
		self.profession2 = profession2