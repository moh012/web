from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('blog_grid', views.blog_grid, name='blog_grid'),
    path('blog_single', views.blog_single, name='blog_single'),
    path('chat', views.chat, name='chat'),
    path('contact', views.contact, name='contact'),
    path('report_property/<int:id_property>',
         views.report_property,
         name='report_property'),
    path('report_order/<int:id_order>',
         views.report_order,
         name='report_order'),
]