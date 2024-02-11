from django.shortcuts import render
from order.models import Order
from accounts.models import Customer
from property.models import Area

# Create your views here.


def order(request):
    if request.method == 'POST':
        customer = Customer(id=1)
        title = request.POST.get('orderTitle')
        orderType = request.POST.get('orderType')
        area = Area(id=1)
        location = request.POST.get('location')
        minPrice = request.POST.get('minPrice')
        maxPrice = request.POST.get('maxPrice')
        room = request.POST.get('room')
        hall = request.POST.get('hall')
        bathroom = request.POST.get('bathroom')
        floor = request.POST.get('floor')
        street = request.POST.get('street')
        propertyAge = request.POST.get('propertyAge')
        houseType = request.POST.get('houseType')
        space = request.POST.get('space')
        description = request.POST.get('description')
        pool = request.POST.get('pool')
        kitchen = request.POST.get('kitchen')
        roof = request.POST.get('roof')
        yard = request.POST.get('yard')
        elev = request.POST.get('elev')
        basement = request.POST.get('basement')
        furnish = request.POST.get('furnish')
        modern = request.POST.get('modern')
        data = Order(
            customer=customer,
            title=title,
            order_type=orderType,
            #  city=city,
            area=area,
            start_price=minPrice,
            end_price=maxPrice,
            room_number=room,
            floor=floor,
            location=location,
            details=description,
            build_year=propertyAge,
            bathrooms=bathroom,
            hall_room=hall,
            floor_room=floor,
            housetype=houseType,
            basement=basement,
            pool=pool,
            kitchen=kitchen,
            furnished=furnish,
            elevator=elev,
            street_number=street,
            appendix=yard,
            roof=roof,
            modern=modern,
            space=space)
        data.save()
    return render(request, 'order/order.html')


def fave(request):
    return render(request, 'order/fave.html')


def order_grid(request):

    context = {
        'orders': Order.objects.all(),
    }

    return render(request, 'order/order_grid.html', context)


def order_single(request):

    context = {
        'orders': Order.objects.all(),
    }

    return render(request, 'order/order_single.html', context)


def serious_order(request):
    return render(request, 'order/serious_order.html')
