from dashboard.models import College
from dashboard.analytics import *

f=open('college.csv')
for i in f.read().strip().split('\n'):
		j=i.split(',')
		collegeobj=College(title=j[0],fees=j[1],exam=j[2],score=j[3],reviews=j[4],specialisation=j[5],location=j[6],ethnicity=j[7],ratings=generate_ratings(j[4]))
		collegeobj.save()