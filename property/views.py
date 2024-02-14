from django.shortcuts import render
from chatting.models import Comment
from accounts.models import Customer, Agent
from django.contrib.auth.models import User
from property.models import Area

# Create your views here.


def property(request):

    return render(request, 'property/property.html')


def property_grid(request):
    if request.method == 'POST':
        type = type.Post.get('type')
        agent = Agent(id=1)
        title = request.POST.get('title')
        propertyType = request.POST.get('propertyType')
        area = Area(id=1)
        location = request.POST.get('location')
        appendix = request.POST.get('appendix')
        price = request.POST.get('price')
        room_number = request.POST.get('room_number')
        hall_room = request.POST.get('hall_room')
        bathrooms = request.POST.get('bathroom')
        floor = request.POST.get('floor')
        street_number = request.POST.get('street_number')
        space = request.POST.get('space')
        description = request.POST.get('description')
        pool = request.POST.get('pool')
        kitchen = request.POST.get('kitchen')
        roof = request.POST.get('roof')
        elevator = request.POST.get('elevator')
        basement = request.POST.get('basement')
        furnished = request.POST.get('furnished')
        build_year = request.POST.get('build_year')
        details = request.POST.get('details')
        type_name = request.POST.get('type_name')
        data = property(
            agent=agent,
            title=title,
            property_type=propertyType,
            #  city=city,
            area=area,
            price=price,
            room_number=room_number,
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
    return render(request, 'property/property_grid.html')


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
