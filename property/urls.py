from django.urls import path
from . import views

urlpatterns = [
    path('property', views.property, name='property'),
    path('property_grid', views.property_grid, name='property_grid'),
    path('property-single', views.property_single, name='property-single'),
  
]