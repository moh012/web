from django.contrib import admin
from .models import Notification
from .models import Financial_Movement
# Register your models here.
admin.site.register(Notification)


class FinancialMovementAdmin(admin.ModelAdmin):
    list_display = ('reference',  'agent', 'customer', 'date_time')
    list_filter = ('agent', 'customer')
    search_fields = ('reference', 'agent__name', 'customer__name')

admin.site.register(Financial_Movement, FinancialMovementAdmin)