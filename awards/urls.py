from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


#Create here
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login/',views.loginuser,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logoutuser,name='logout'),

    path('profile/<id>/',views.profile,name='user_profile'),
    path('profile_update/<str:username>/',views.profile_update,name='profile_update'),

    path('<id>/',views.project_details,name='project-details'),
    path('create_project/new/',views.create_project,name='create_project'),
    path('like_image_design/<user_id>/<project_id>',views.like_project_design, name='like_project_design'),
    path('like_image_usability/<user_id>/<project_id>',views.like_project_usability, name='like_project_usability'),
    path('like_image_content/<user_id>/<project_id>',views.like_project_content, name='like_project_content'),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),


    #Serializer paths
    path('api/profile/', views.ProfileList.as_view()),
    path('api/profile/<int:pk>/', views.ProfileDetail.as_view()),

    path('api/project/', views.ProjectList.as_view()),
    path('api/project/<int:pk>/', views.ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)