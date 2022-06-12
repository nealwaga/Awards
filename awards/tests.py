from django.test import TestCase
from .models import *

# Create your tests here.
class UserProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        # Creating a new editor and saving it
        self.waga= User(id=1, username='waganeal', password='1234')
        self.waga.save_user()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_website= Site(title = 'Test Site',tags = 'This is a random test site',userprofile = self.waga)
        self.new_website.save()

        self.new_website.tags.add(self.new_tag)
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def tearDown(self):
        UserProfile.objects.all().delete()
        tags.objects.all().delete()
        Site.objects.all().delete()


    
    def setUp(self):
        self.user = User(first_name="neal", last_name="waga",
                         username="briankiiru", email="neal@gmail.com",)
        self.user.save()
        self.profile = UserProfile(user=self.user, bio="None")
        self.profile.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))



class RateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='waganeal')
        self.post = Site.objects.create(id=1, title='test post', image='https://i.pinimg.com/736x/c6/45/30/c64530d2d8694b51f5237e3a6273e786.jpg',
                                        developer=self.user, url='http://ur.coml')
        self.rating = Rate.objects.create(id=1, design=6, usability=7, content=9, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rate))

    def test_save_rating(self):
        self.rating.save_rate()
        rating = Rate.objects.all()
        self.assertTrue(len(rating) > 0)