from django.contrib.auth.views import login
from django.conf.urls import url
from .views import home, register, profile, logout_view

urlpatterns = [
    url(r'^$', home),
    url(r'^register/', register),
    url(r'^profile/', profile),
    url(r'^logout/$', logout_view),
    url(r'^login/$', login, {'template_name': 'registration/login.html'}),
]
