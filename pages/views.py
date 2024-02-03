from django.shortcuts import render
from django.template import loader  #اضافتي للمستقبل القريب
from property.models import City, Property
from order.models import Order
from django.contrib.auth.models import User

# Create your views here.


def index(request):

    context = {
        'citys': City.objects.all(),
        'alluser': User.objects.all().count(),
        'allproperty': Property.objects.all().count(),
        'allorder': Order.objects.all().count(),
    }

    return render(request, 'pages/index.html', context)
    #template = loader.get_template('index.html')
