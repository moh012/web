from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createAccount', views.createAccount, name='createAccount'),
    path('logIn', views.logIn, name='logIn'),
    path('phoneNumber', views.phoneNumber, name='phoneNumber'),
    path('verificationCode', views.verificationCode, name='verificationCode'),
]