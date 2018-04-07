from django.conf.urls import include, url
<<<<<<< HEAD
from .views import home, colleges, recommendations, counsellors, profile,chat
=======
from .views import home, colleges, recommendations, counsellors, profile, counsellors_profile, college_profile
>>>>>>> 4b075e2323474cc9baac381bf59da4a0aebe4f82

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^colleges/$', colleges),
	url(r'^recommendations/$',recommendations),
	url(r'^counsellors/$', counsellors),
	url(r'^profile/', profile),
	url(r'^chat/',chat),
	url(r'^counsellors_profile/(?P<counsellor_username>[\w\-]+)/$', counsellors_profile, name='counsellors_profile'),
	url(r'^college_profile/(?P<number>\d+)/$', college_profile, name='college_profile')

]
