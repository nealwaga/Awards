from django.urls import re_path as url
from django.conf.urls import include
from . import views


#Create url patterns here
urlpatterns = [
    url('^$', views.site_today, name='siteToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_site, name='pastSite'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^site(\d+)', views.site, name ='site')
]