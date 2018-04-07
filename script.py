from dashboard.models import Counsellor, Passout
from dashboard.analytics import generate_ratings
from random import choice

colleges = Counsellor.objects.all()
f = open('a.csv')
for col in f.read().strip().split('\n'):
	colobj = Passout(name=col.strip(), counsellor_username=choice(colleges).user.username)
	colobj.save()
f.close()