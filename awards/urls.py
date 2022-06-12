from django.urls import re_path as url
from django.conf.urls import include
from . import views


#Create url patterns here
urlpatterns = [
    url('^$', views.site_today, name='siteToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_days_site, name='pastSite'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^site(\d+)', views.site, name ='site'),
    url(r'^new/site$', views.new_site, name='new-site'),
    url('site_rate/<int:pk>/',views.site_rate,name="site_rate"),
    url(r"^profile/(\d+)", views.profile, name="profile"),
    url(r'^myprofile/$',views.my_profile,name = 'my-profile'),
    url(r'^register/$',views.register,name='register'),
    url(r'^createprofile/$',views.create_profile,name = 'create-profile'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^accounts/login/$',views.user_login,name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]