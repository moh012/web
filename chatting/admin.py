from django.contrib import admin
from .models import Chat, Report_Agent, Report_Customer, Evaluation, Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    search_fields = ['username']


admin.site.register(Chat)
admin.site.register(Report_Agent)
admin.site.register(Report_Customer)
admin.site.register(Evaluation)
admin.site.register(Contact, ContactAdmin)
