from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order, name='order'),
    path('order_grid', views.order_grid, name='order_grid'),
    path('order_single/<int:id>', views.order_single, name='order_single'),
    path('fave', views.fave, name='fave'),
    path('add-fave/<int:id_property>/', views.add_fave, name='add_fave'),
    path('rm_fave/<int:id>', views.rm_fave, name='rm_fave'),
    # path('serious_order/<int:id>', views.serious_order, name='serious_order'),
    path('edit_order/<int:id>', views.edit_order, name='edit_order'),
    path('delete_order/<int:id>', views.delete_order, name='delete_order'),
    path('my_order/<int:id>', views.my_order, name='my_order'),
]