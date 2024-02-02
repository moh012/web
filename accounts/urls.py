from django.urls import path
from . import views

urlpatterns = [
    path('agents_grid', views.agents_grid, name='agents_grid'),
    path('agent_single', views.agent_single, name='agent_single'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('userdata', views.userdata, name='userdata'),
    path('verification', views.verification, name='verification'),
]