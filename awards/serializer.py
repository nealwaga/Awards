from dataclasses import fields
from rest_framework import serializers
from .models import *


#Create here
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'user', 'bio']
        

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['developer', 'url', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'url']