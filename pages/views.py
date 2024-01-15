from django.shortcuts import render

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
    return render(request, 'pages/contact.html')


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def order_grid(request):
    return render(request, 'pages/order-grid.html')


def order_single(request):
    return render(request, 'pages/order-single.html')


def property_grid(request):
    return render(request, 'pages/property-grid.html')


def property_single(request):
    return render(request, 'pages/property-single.html')


def fave(request):
    return render(request, 'pages/fave.html')

