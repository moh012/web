from django.urls import path
from . import views
urlpatterns = [
     path('payment/<int:pay_id>', views.payment, name='payment'),

]
