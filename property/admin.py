from django.contrib import admin
from .models import Type, City, Area, Property, Photo_Property, Comparison, Favorite, ADS, Photo_ADS

# Register your models here.
admin.site.register(Type)
admin.site.register(City)
admin.site.register(Area)
admin.site.register(Property)
admin.site.register(Photo_Property)
admin.site.register(Comparison)
admin.site.register(Favorite)
admin.site.register(ADS)
admin.site.register(Photo_ADS)