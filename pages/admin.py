from django.contrib import admin
from .models import User, Notification, Financial_Movement, Comparison, Photo_Property, Favorite, ADS, Photo_ADS, Evaluation, Report_Customer

# Register your models here.

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(Financial_Movement)
admin.site.register(Comparison)
admin.site.register(Photo_Property)
admin.site.register(Favorite)
admin.site.register(ADS)
admin.site.register(Photo_ADS)
admin.site.register(Evaluation)
admin.site.register(Report_Customer)