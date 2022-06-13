from dataclasses import fields
from django.forms import ModelForm,TextInput
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Create here
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False


class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        # fields = ['title','description','project_image','project_url','location']
        fields = ['title','description','project_image','project_url']

        def __init__(self,*args, **kwargs):
            super(ProjectUploadForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['prof_pic','bio','website','name','phone', 'linkedin']

        def __init__(self, *args, **kwargs):
            super(ProfileUpdateForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
