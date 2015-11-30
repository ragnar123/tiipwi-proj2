from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/([0-9]{4})', 'weather_station.views.info'), 
    url(r'^list', 'weather_station.views.list'), 
    url(r'^signup', 'weather_station.views.signup'), 
    url(r'/*', 'weather_station.views.index'),
)
