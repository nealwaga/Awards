from django.contrib import admin
from .models import *

# from mapbox_location_field.admin import MapAdmin  


# Register your models here.
admin.site.register(Profile)
# admin.site.register(Project,MapAdmin)
admin.site.register(Project)
admin.site.register(UsabilityVote)
admin.site.register(ContentVote)
admin.site.register(DesignVote)
admin.site.register(Comment)