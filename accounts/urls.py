from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('agents_grid', views.agents_grid, name='agents_grid'),
    path('agent_single', views.agent_single, name='agent_single'),
    path('login', views.login, name='login'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('signup', views.signup, name='signup'),
    path('userdata', views.userdata, name='userdata'),
    path('verification', views.verification, name='verification'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    
]