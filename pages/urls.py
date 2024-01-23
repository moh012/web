from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('agent-single', views.agent_single, name='agent-single'),
    path('agents-grid', views.agents_grid, name='agents-grid'),
    path('blog-grid', views.blog_grid, name='blog-grid'),
    path('blog-single', views.blog_single, name='blog-single'),
    path('contact', views.contact, name='contact'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('order', views.order, name='order'),
    path('order-grid', views.order_grid, name='order-grid'),
    path('order-single', views.order_single, name='order-single'),
    path('serious_order', views.serious_order, name='serious_order'),
    path('property', views.property, name='property'),
    path('property-grid', views.property_grid, name='property-grid'),
    path('property-single', views.property_single, name='property-single'),
    path('fave', views.fave, name='fave'),
    path('userdata', views.userdata, name='userdata'),
    path('verification', views.verification, name='verification'),
]