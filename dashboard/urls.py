from django.conf.urls import include, url
from .views import home,colleges

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^colleges/$', colleges),
]
