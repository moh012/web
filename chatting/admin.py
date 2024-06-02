from django.contrib import admin
from .models import Chat, Report_Agent, Report_Customer, Evaluation, Contact, Comment
from .models import Message
# Register your models here.

#خاص برسائل الدردشة
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message', 'timestamp']
    search_fields = ['sender__username', 'receiver__username']
    list_filter = ['timestamp']

admin.site.register(Message, MessageAdmin)




class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    search_fields = ['username']
    list_filter = ['username', 'email']
    list_display_links = ['id', 'username']


admin.site.register(Chat)
admin.site.register(Report_Agent)
admin.site.register(Report_Customer)
admin.site.register(Evaluation)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment)
