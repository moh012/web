from django.shortcuts import get_object_or_404, render
from django.template import loader  #اضافتي للمستقبل القريب
from property.models import City, Property, Area
from order.models import Order, Booking
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    context = {
        'city': City.objects.all(),
        'area': Area.objects.all(),
        'alluser': User.objects.all().count(),
        'allproperty': Property.objects.all().count(),
        'allorder': Order.objects.all().count(),
        'allbooking': Booking.objects.all().count(),
    }

    return render(request, 'pages/index.html', context)
