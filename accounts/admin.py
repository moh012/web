from django.contrib import admin
from .models import Agent, Customer


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


# Register your models here.
admin.site.register(Agent, ContactAdmin)
admin.site.register(Customer, ContactAdmin)
