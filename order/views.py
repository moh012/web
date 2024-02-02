from django.shortcuts import render
from order.models import Order

# Create your views here.


def order(request):
    if request.method == 'POST':
        title = request.POST.get('rental')
    return render(request, 'order/order.html')

def fave(request):
    return render(request, 'order/fave.html')


def order_grid(request):

    context = {
        'orders': Order.objects.all(),
    }

    return render(request, 'order/order_grid.html', context)


def order_single(request):
    return render(request, 'order/order_single.html')


def serious_order(request):
    return render(request, 'order/serious_order.html')

