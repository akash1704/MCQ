from django.contrib import admin

# Register your models here.
from mcqapp.models import UserProfileInfo, User

admin.site.register(UserProfileInfo)

#When you edit admin.py file or create a new model, remember to migrate
