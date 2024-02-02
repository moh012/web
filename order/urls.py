from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order, name='order'),
    path('order_grid', views.order_grid, name='order_grid'),
    path('order_single', views.order_single, name='order_single'),
    path('fave', views.fave, name='fave'),
    path('serious_order', views.serious_order, name='serious_order'),
]