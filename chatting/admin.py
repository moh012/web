from django.contrib import admin
from .models import Chat, Report_Agent, Report_Customer, Evaluation

# Register your models here.
admin.site.register(Chat)
admin.site.register(Report_Agent)
admin.site.register(Report_Customer)
admin.site.register(Evaluation)