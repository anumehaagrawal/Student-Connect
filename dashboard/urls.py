from django.conf.urls import include, url
from .views import home, colleges, recommendations, counsellors, profile, counsellors_profile, college_profile,chat

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
