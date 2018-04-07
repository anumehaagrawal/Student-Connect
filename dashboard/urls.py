from django.conf.urls import include, url
from .views import home, colleges, recommendations, counsellors, profile,chat

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^colleges/$', colleges),
	url(r'^recommendations/$',recommendations),
	url(r'^counsellors/$', counsellors),
	url(r'^profile/', profile),
	url(r'^chat/',chat),
	
]
