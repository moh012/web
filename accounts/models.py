from django.db import models
from django.conf import settings
import datetime
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
    profil_photo = models.ImageField(upload_to=filepath1, blank=True)
    state = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.profil_photo:
            self.profil_photo = 'uploads/avatar.png'
        super().save(*args, **kwargs)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to=filepath1, blank=True)
    state = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username
    
    
    def save(self, *args, **kwargs):
        # التحقق مما إذا كانت الصورة محددة
        if not self.photo:  
            # في حالة عدم تحديد الصورة، استخدم الصورة الافتراضية
            self.photo = 'uploads/avatar.png'
        super().save(*args, **kwargs)
