from django.urls import path
from . import views
urlpatterns = [
       path('fave', views.fave, name='fave'),
]
