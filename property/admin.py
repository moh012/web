from django.contrib import admin
from .models import City, Area, Property, Photo_Property, Comparison, Favorite, ADS, Photo_ADS

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_name']


class ContactAdmin1(admin.ModelAdmin):
    list_display = ['id', 'agent', 'title', 'property_type']
    list_display_links = ['id', 'agent', 'title', 'property_type']


# admin.site.register(Type)
admin.site.register(City, ContactAdmin)
admin.site.register(Area)
admin.site.register(Property, ContactAdmin1)
admin.site.register(Photo_Property)
admin.site.register(Comparison)
admin.site.register(Favorite)
admin.site.register(ADS)
admin.site.register(Photo_ADS)