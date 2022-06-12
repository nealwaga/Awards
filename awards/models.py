from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfile (models.Model):
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField ('profile_pic')
    phone_number = models.IntegerField (max_length=10, blank=False)
    bio = models.TextField (blank=False)

    def __str__(self):
        return self.user.first_name

    def save_userprofile(self):
        self.save()

    def delete_userprofile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()


class tags(models.Model):
    name = models.CharField (max_length=10)

    def __str__(self):
        return self.name