from django.contrib.auth.models import User
from django.db import  models
import os
from collectivework.settings import MEDIA_URL

# Pillow paketi gerekli

def get_image_path(instance, filename):
    return os.path.join(MEDIA_URL, 'images', str(instance.user.id), filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User) #1e 1 ilişkisi var
    #city = models.CharField(max_length=45)
    profilephoto = models.ImageField(upload_to=get_image_path,blank=True, null=True)
