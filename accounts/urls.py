from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('agent_single/<int:id>', views.agent_single, name='agent_single'),
    path('agents_grid', views.agents_grid, name='agents_grid'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('signup', views.signup, name='signup'),
    path('userdata', views.userdata, name='userdata'),
    path('verification', views.verification, name='verification'),
    path('change_password/',
         auth_views.PasswordChangeView.as_view(
             template_name='accounts/change_password.html'),
         name='change_password'),
    path('password_change_done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('pyment', views.pyment, name='pyment'),

]