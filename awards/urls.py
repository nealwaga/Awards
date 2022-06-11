from django.conf.urls import url, include
from . import views


#Create url patterns here
urlpatterns = [
    url('^$', views.site_today, name='siteToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_site, name='pastSite')
]