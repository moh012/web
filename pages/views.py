from django.shortcuts import render
from chatting.models import Contact

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


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
    return render(request, 'pages/order.html')


def order_grid(request):
    return render(request, 'pages/order-grid.html')


def order_single(request):
    return render(request, 'pages/order-single.html')


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
