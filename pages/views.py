from django.shortcuts import render
from django.template import loader  #اضافتي للمستقبل القريب
from chatting.models import Contact
from property.models import City
from django.http import HttpResponse
from order.models import Order

# Create your views here.


def index(request):

    context = {
        'citys': City.objects.all(),
        'allorder': Order.objects.all().count(),
    }

    #template = loader.get_template('index.html')
    return render(request, 'pages/index.html', context)

    #return HttpResponse(template.render(context, request))


def about(request):
    return render(request, 'pages/about.html')


def agent_single(request):
    return render(request, 'pages/agent-single.html')


def agents_grid(request):
    return render(request, 'pages/agents-grid.html')


def blog_grid(request):
    return render(request, 'pages/blog-grid.html')


def blog_single(request):
    return render(request, 'pages/blog-single.html')


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(username=username,
                       email=email,
                       subject=subject,
                       message=message)
        data.save()

    return render(request, 'pages/contact.html')


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def signup(request):
    return render(request, 'pages/signup.html')


def order(request):
    if request.method == 'POST':
        title = request.POST.get('rental')
    return render(request, 'pages/order.html')


def order_grid(request):

    context = {
        'orders': Order.objects.all(),
    }

    return render(request, 'pages/order-grid.html', context)


def order_single(request):
    return render(request, 'pages/order-single.html')


def serious_order(request):
    return render(request, 'pages/serious_order.html')


def property(request):
    return render(request, 'pages/property.html')


def property_grid(request):
    return render(request, 'pages/property-grid.html')


def property_single(request):
    return render(request, 'pages/property-single.html')


def fave(request):
    return render(request, 'pages/fave.html')


def userdata(request):
    return render(request, 'pages/userdata.html')


def verification(request):
    return render(request, 'pages/verification.html')
