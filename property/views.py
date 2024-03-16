from django.shortcuts import render
from chatting.models import Comment
from accounts.models import Customer, Agent
from django.contrib.auth.models import User
from property.models import Area, Property

# Create your views here.


def property(request):
    if request.method == 'POST':
        agent = Agent(id=1)
        title = request.POST.get('property')
        propertyType = request.POST.get('propertyType')
        area = Area(id=1)
        location = request.POST.get('location_property')
        img = request.POST.get('image_property')
        description = request.POST.get('description')
        price = request.POST.get('price_property')
        room_number = request.POST.get('room_property')
        hall_room = request.POST.get('hall_property')
        bathrooms = request.POST.get('bathroom_property')
        floor = request.POST.get('floor_property')
        street_number = request.POST.get('street_property')
        build_year = request.POST.get('propertyAge')
        house_type = request.POST.get('AccommodationType')
        space = request.POST.get('space')
        pool = request.POST.get('pool_property')
        kitchen = request.POST.get('kitchen_property')
        roof = request.POST.get('Roof_property')
        modern = request.POST.get('new_property')
        yard = request.POST.get('yard_property')
        elevator = request.POST.get('elevator_property')
        basement = request.POST.get('basement_property')
        furnished = request.POST.get('Furnished_property')
        data = Property(
            agent=agent,
            title=title,
            property_type=propertyType,
            #  city=city,
            area=area,
            price=price,
            room_number=room_number,
            floor=floor,
            location=location,
            img=img,
            description=description,
            build_year=build_year,
            bathrooms=bathrooms,
            hall_room=hall_room,
            house_type=house_type,
            basement=basement,
            pool=pool,
            kitchen=kitchen,
            furnished=furnished,
            elevator=elevator,
            street_number=street_number,
            appendix=yard,
            roof=roof,
            modern=modern,
            space=space)
        data.save()

    return render(request, 'property/property.html')


def property_grid(request):

    context = {
        'properties': Property.objects.all(),
    }

    return render(request, 'property/property_grid.html', context)


def property_single(request):

    if request.method == 'POST':
        customer = Customer()
        comment = request.POST.get('message')
        data = Comment(customer=customer, comment=comment)
        data.save()

    context = {
        'cuscomment': Comment.objects.all(),
        'commentnum': Comment.objects.all().count(),
        'cust': Customer.objects.all(),
    }

    return render(request, 'property/property_single.html', context)
