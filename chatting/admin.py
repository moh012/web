from django.contrib import admin
from .models import Chat, Order, Booking, Area, City, Property, Type, Report_Agent

# Register your models here.
admin.site.register(Chat)
admin.site.register(Order)
admin.site.register(Booking)
admin.site.register(Area)
admin.site.register(City)
admin.site.register(Property)
admin.site.register(Type)
admin.site.register(Report_Agent)