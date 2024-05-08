from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('agent_single/<int:id>', views.agent_single, name='agent_single'),
    path('agents_grid', views.agents_grid, name='agents_grid'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('signup', views.signup, name='signup'),
    path('userdata', views.userdata, name='userdata'),
    path('verification', views.verification, name='verification'),
]