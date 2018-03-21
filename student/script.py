from student.models import College
from student.analytics import generate_ratings
"""
f = open('counsellors.csv')
for j in f.read().split('\n')[1:]:
	col = Counsellor()
	i = j.split(',')
	col.name=i[0]
	col.university=i[1]
	col.contact=i[2]
	col.save()
"""

for a in College.objects.all():
	a.ratings = generate_ratings(a.reviews)
	a.save()
