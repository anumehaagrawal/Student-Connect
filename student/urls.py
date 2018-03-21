from django.contrib.auth.views import login
from django.conf.urls import url
from .views import home, colleges, register, profile, logout_view, recommendations, counsellors

urlpatterns = [
	url(r'^$', home),
	url(r'^counsellors/', counsellors),
	url(r'^recommendations/', recommendations),
	url(r'^colleges/', colleges),
	url(r'^register/', register),
	url(r'^profile/', profile),
	url(r'^logout/$', logout_view),
	url(r'^login/$', login, {'template_name': 'registration/login.html'}),
]
