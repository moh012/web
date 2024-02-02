from django.shortcuts import render
from django.template import loader  #اضافتي للمستقبل القريب
from property.models import City
from order.models import Order

# Create your views here.

def index(request):

    context = {
        'citys': City.objects.all(),
        'allorder': Order.objects.all().count(),
    }

    return render(request, 'pages/index.html')
    #template = loader.get_template('index.html')

