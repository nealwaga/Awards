from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register (UserProfile)
admin.site.register (Rate)
admin.site.register (Site)
admin.site.register (tags)


#Create here
class SiteAdmin(admin.ModelAdmin):
    filter_horizontal =('tags', )


class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'bio', 'phone_number', 'is_mvp']
    list_editable=[ 'bio', 'phone_number', 'is_mvp']