
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import datetime
from django.utils.text import slugify

import os

# Create your models here.


def filepath1(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)


#extend Agent class form User class
class Agent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    profil_photo = models.ImageField(upload_to=filepath1,
                                     blank=True,
                                     default='uploads/avatar.png')
    state = models.BooleanField(default=False, null=True)
    who_i = models.CharField(_("نبذة عني :"),max_length=250 , blank=True , null=True)
    address = models.CharField(_("العنوان  :"),max_length=250 , blank=True , null=True)
    facebook = models.CharField(max_length=100 , blank=True , null=True)
    instagram = models.CharField(max_length=100 , blank=True , null=True)
    twitter = models.CharField(max_length=100 , blank=True , null=True)

    def __str__(self):
        return self.user.username
        


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to=filepath1,
                              blank=True,
                              default='uploads/avatar.png')
    state = models.BooleanField(default=False, null=True)
    facebook = models.CharField(max_length=100 , blank=True , null=True)
    instagram = models.CharField(max_length=100 , blank=True , null=True)
    twitter = models.CharField(max_length=100 , blank=True , null=True)

    def __str__(self):
        return self.user.username
