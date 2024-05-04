from django.contrib import admin
from .models import Order, Booking

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'title', 'order_type']
    list_display_links = ['id', 'customer', 'title', 'order_type']


admin.site.register(Order, ContactAdmin)
admin.site.register(Booking)