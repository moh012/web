from django.shortcuts import render, redirect
from order.models import Order
from accounts.models import Customer
from property.models import Area, City
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


def order(request):

    context = {
        'city': City.objects.all(),
        'area': Area.objects.all(),
    }

    if request.method == 'POST':
        customer = request.user.customer
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
        messages.success(request, "تم إضافة الطلب بنجاح!")
        return redirect('order_grid')

    return render(request, 'order/order.html', context)


def fave(request):
    return render(request, 'order/fave.html')


def order_grid(request):

    context = {
        'orders': Order.objects.all(),
    }

    return render(request, 'order/order_grid.html', context)


def order_single(request, id):
    ord = Order.objects.get(id=id)

    context = {
        'orders': Order.objects.all(),
        'ord': ord,
    }

    return render(request, 'order/order_single.html', context)


@login_required(login_url='login')
def serious_order(request, id):
    ord = Order.objects.get(id=id)

    if request.method == "POST":
        ord.state = True
        ord.save()
        messages.success(request, "تم ترقية طلبك إلى طلب جاد!")
        return redirect('order_grid')

    return render(request, 'order/serious_order.html')


@login_required(login_url='login')
def edit_order(request, id):
    ord = Order.objects.get(id=id)

    if request.method == "POST":
        ord.title = request.POST.get('orderTitle')
        ord.order_type = request.POST.get('orderType')
        ord.location = request.POST.get('location')
        ord.start_price = request.POST.get('minPrice')
        ord.end_price = request.POST.get('maxPrice')
        ord.room_number = request.POST.get('room')
        ord.hall_room = request.POST.get('hall')
        ord.bathrooms = request.POST.get('bathroom')
        ord.floor = request.POST.get('floor')
        ord.street_number = request.POST.get('street')
        ord.build_year = request.POST.get('propertyAge')
        ord.housetype = request.POST.get('houseType')
        ord.space = request.POST.get('space')
        ord.details = request.POST.get('description')
        ord.pool = request.POST.get('pool')
        ord.kitchen = request.POST.get('kitchen')
        ord.roof = request.POST.get('roof')
        ord.modern = request.POST.get('yard')
        ord.appendix = request.POST.get('elev')
        ord.elevator = request.POST.get('basement')
        ord.basement = request.POST.get('furnish')
        ord.furnished = request.POST.get('modern')
        ord.save()
        messages.success(request, "تم تعديل الطلب بنجاح!")
        return redirect('order_grid')
    context = {'ord': ord}
    return render(request, 'order/edit_order.html', context)


@login_required(login_url='login')
def delete_order(request, id):
    ord = Order.objects.get(id=id)
    if request.method == "POST":
        ord.delete()
        messages.success(request, "تم حذف الطلب بنجاح!")
        return redirect('order_grid')
    context = {'ord': ord}
    return render(request, 'order/delete_order.html', context)


@login_required(login_url='login')
def my_order(request, id):
    cust = Customer.objects.get(id=id)
    orders = cust.orders.all()
    num_orders = orders.count()
    context = {'cust': cust, 'orders': orders, 'num_orders': num_orders}
    return render(request, 'order/my_order.html', context)