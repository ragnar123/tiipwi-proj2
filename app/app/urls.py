from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^put_reading/([0-9]{4})/(\w+)/(\d+?\.?\d+)/$', 'weather_station.views.put_reading'),
    url(r'^plots/([0-9]{4})/', 'weather_station.views.plot'),
    url(r'^info/([0-9]{4})', 'weather_station.views.info'),
    url(r'^list', 'weather_station.views.list'),
    url(r'^signup', 'weather_station.views.signup'),
    url(r'/*', 'weather_station.views.index'),
)
