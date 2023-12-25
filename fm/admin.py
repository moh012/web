from django.contrib import admin
from .models import Notification, Financial_Movement

# Register your models here.
admin.site.register(Notification)
admin.site.register(Financial_Movement)