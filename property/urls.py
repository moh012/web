from django.urls import path
from . import views

urlpatterns = [
    path('property', views.property, name='property'),
    path('property_grid', views.property_grid, name='property_grid'),
    path('property_single/<int:id>',
         views.property_single,
         name='property_single'),
    path('edit_property/<int:id>', views.edit_property, name='edit_property'),
    path('delete_property/<int:id>',
         views.delete_property,
         name='delete_property'),
    path('my_property/<int:id>', views.my_property, name='my_property'),
]