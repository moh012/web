from django.db import models

# Create your models here.


class User(models.Modle):
    name = models.CharField(max_length=50)
    content = models.TextField()