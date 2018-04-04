from django.conf.urls import include, url
from .views import home,colleges, recommendations

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^colleges/$', colleges),
	url(r'^recommendations/$',recommendations),
]
