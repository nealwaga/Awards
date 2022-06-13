from django.db import models
from django.contrib.auth.models import User
# from mapbox_location_field.models import LocationField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    prof_pic = models.ImageField(blank=True, upload_to='media')
    bio = models.TextField(blank=True, max_length=255)
    website = models.URLField(blank=True, max_length=50)
    name = models.CharField(blank=True, max_length=50)
    phone = PhoneNumberField(blank=True)
    fax_number = PhoneNumberField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.name

    def save_profile(self):
        '''Add Profile to database'''
        self.save()


class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    title = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=True, max_length=500)
    project_image = models.ImageField(blank=False, upload_to='media')
    project_url = models.URLField(blank=False, max_length=255)
    created_on = models.DateField(auto_now_add=True)
    # location = LocationField(blank=True)

    def __str__(self):
        return self.title

    def save_project(self):
        '''Add new project'''
        self.save()

    @classmethod
    def delete_project(cls,id):
        ''' Delete project from database '''
        project = Project.objects.get(id=id)
        project.delete()

    @property
    def saved_likes_design(self):
        return self.design_likes.count()

    @property
    def saved_likes_usability(self):
        return self.usability_likes.count()

    @property
    def saved_likes_content(self):
        return self.content_likes.count()


class Comment(models.Model):
    user_profile = models.ForeignKey(Profile, null=True,on_delete=models.SET_NULL)
    user_comment = models.CharField(blank=False, max_length=255)
    project_associated = models.ForeignKey(Project, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.user_comment

    def save_comment(self):
        '''Add Comment to database'''
        self.save()

    @classmethod
    def delete_comment(cls,id):
        ''' Delete comment from database '''
        comment = Comment.objects.get(id=id)
        comment.delete()


# Design Usability Content
class DesignVote(models.Model):
    profile_vote = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    post_voted = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL, related_name='design_likes')

    def save_like(self):
        self.save()

class UsabilityVote(models.Model):
    profile_vote = models.ForeignKey(Profile, null=True,on_delete=models.SET_NULL)
    post_voted = models.ForeignKey(Project, null=True,on_delete=models.SET_NULL, related_name='usability_likes')

    def save_like(self):
        self.save()

class ContentVote(models.Model):
    profile_vote = models.ForeignKey(Profile, null=True,on_delete=models.SET_NULL)
    post_voted = models.ForeignKey(Project, null=True,on_delete=models.SET_NULL, related_name='content_likes')

    def save_like(self):
        self.save()