from django.db import models
#import basic user models
from django.contrib.auth.models import User


# Create your models here.
class User:
    total_score = models.IntegerField(default=0)


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional attributes
    portfolio_site = models.URLField(blank=True)

    #Pillow library should be installed for ImageField - pip install pillow
    profile_pic = models.ImageField(upload_to='mcqapp/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
