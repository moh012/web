from django.shortcuts import render, redirect, get_object_or_404
from order.models import Order
from accounts.models import Customer
from property.models import Area
from property.models import City
from property.models import Favorite
from property.models import Property
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


@login_required(login_url='login')
def order(request):

    context = {
        'city': City.objects.all(),
        'area': Area.objects.all(),
    }

    ord = Order()

    if request.method == 'POST':
        ord.customer = request.user.customer
        ord.title = request.POST.get('orderTitle')
        ord.order_type = request.POST.get('orderType')
        ord.area = Area(id=request.POST.get('area'))
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
        messages.success(request, "تم إضافة الطلب بنجاح!")
        return redirect('order_grid')

    return render(request, 'order/order.html', context)


def fave(request):

    context = {
        'fave': Favorite.objects.all(),
    }

    return render(request, 'order/fave.html', context)


def add_fave(request, id_property):
    try:
        property_obj = get_object_or_404(Property, id=id_property)
        fave, created = Favorite.objects.get_or_create(
            property=property_obj, customer=request.user.customer, status=True)
        if created:
            messages.success(request, "تم إضافة العقار إلى المفضلة!")
        else:
            messages.info(request, "العقار موجود بالفعل في المفضلة!")
    except Exception as e:
        messages.error(request, f"حدث خطأ: {e}")
    return redirect('fave')


def rm_fave(request, id):
    fave = Favorite.objects.filter(id=id)
    fave.delete()
    messages.error(request, "تم إزالة العقار من المفضلة!")
    return redirect('fave')


def order_grid(request):
    try:
        search = Order.objects.all().order_by('-id')
        title = None
        if 'search_name' and 'search_type' and 'search_bathroom' in request.GET:
            title = request.GET['search_name']
            order_type = request.GET['search_type']
            search_room = request.GET['search_room']
            search_bathroom = request.GET['search_bathroom']
            if title:
                search = search.filter(
                    title__icontains=title,
                    order_type__icontains=order_type,
                    room_number__icontains=search_room,
                    bathrooms__icontains=search_bathroom,
                )
    except Exception as e:
        messages.error(request, f"حدث خطأ: {e}")

    context = {
        'orders': search,
    }

    return render(request, 'order/order_grid.html', context)


@login_required(login_url='login')
def order_single(request, id):
    ord = Order.objects.get(id=id)

    context = {
        'orders': Order.objects.all(),
        'ord': ord,
    }

    return render(request, 'order/order_single.html', context)


# @login_required(login_url='login')
# def serious_order(request, id):
#     ord = Order.objects.get(id=id)

#     if request.method == "POST":
#         ord.state = True
#         ord.save()
#         messages.success(request, "تم ترقية طلبك إلى طلب جاد!")
#         return redirect('order_grid')

#     return render(request, 'order/serious_order.html')


@login_required(login_url='login')
def edit_order(request, id):
    ord = Order.objects.get(id=id)

    if request.method == "POST":
        ord.title = request.POST.get('orderTitle')
        ord.order_type = request.POST.get('orderType')
        ord.area = Area(id=request.POST.get('area'))
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
        messages.warning(request, "تم تعديل الطلب بنجاح!")
        return redirect('order_grid')
    context = {
        'ord': ord,
        'city': City.objects.all(),
        'area': Area.objects.all(),
    }
    return render(request, 'order/edit_order.html', context)


@login_required(login_url='login')
def delete_order(request, id):
    ord = Order.objects.get(id=id)
    if request.method == "POST":
        ord.delete()
        messages.error(request, "تم حذف الطلب بنجاح!")
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