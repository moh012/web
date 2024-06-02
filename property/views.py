from django.shortcuts import render, redirect ,get_object_or_404
from chatting.models import Comment
from chatting.forms  import CommentForm
from accounts.models import Customer, Agent
from django.contrib.auth.models import User
from property.models import Area, Property
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


def property(request):
    if request.method == 'POST':
        agent = request.user.agent
        title = request.POST.get('property')
        propertyType = request.POST.get('propertyType')
        area = Area(id=1)
        location = request.POST.get('location_property')
        if len(request.FILES) != 0:
            img = request.FILES['image_property']
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
            details=description,
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
        messages.success(request, "تم إضافة العقار بنجاح!")
        return redirect('property_grid')

    return render(request, 'property/property.html')


def property_grid(request):

    context = {
        'properties': Property.objects.all(),
    }

    return render(request, 'property/property_grid.html', context)


# def property_single(request, property_id):
#     property = get_object_or_40   4(Property, id=property_id)
#     comments = property.comments.filter(parent_comment__isnull=True)  # فقط التعليقات الرئيسية

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.customer = request.user.customer
#             comment.property = property
#             comment.save()
#             return redirect('property_single', property_id=property.id)
#     else:
#         form = CommentForm()
    
#     context = {
#         'comment_num': Comment.objects.all().count(),
#         'property': property,
#         'comments': comments,
#         'form': form
#     }
#     return render(request, 'property/property_single.html', context)




# @login_required
# def reply_to_comment(request, comment_id):
#     parent_comment = get_object_or_404(Comment, id=comment_id)
#     property = parent_comment.property
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             reply = form.save(commit=False)
#             reply.customer = request.user.customer
#             reply.property = property
#             reply.parent_comment = parent_comment
#             reply.is_reply = True
#             reply.save()
#             return redirect('property_single', property_id=property.id)
#     else:
#         form = CommentForm()
    
#     context = {
#         'form': form,
#         'property': property,
#         'parent_comment': parent_comment
#     }
#     return render(request, 'property/reply_to_comment.html', context)


@login_required
def property_single(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    comments = property.comments.filter(parent_comment__isnull=True) 

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if hasattr(request.user, 'customer'):
                comment.customer = request.user.customer
            elif hasattr(request.user, 'agent'):
                comment.agent = request.user.agent
            comment.property = property
            comment.save()
            return redirect('property_single', property_id=property.id)
    else:
        form = CommentForm()
    
    context = {
        'comment_num': Comment.objects.filter(property_id=property_id).count(),
        'property': property,
        'comments': comments,
        'form': form
    }
    return render(request, 'property/property_single.html', context)


@login_required
def reply_to_comment(request, comment_id):
    parent_comment = get_object_or_404(Comment, id=comment_id)
    property = parent_comment.property

    if request.method == 'POST':
        form = CommentForm(request.POST)    
        if form.is_valid():
            reply = form.save(commit=False)
            if hasattr(request.user, 'customer'):
                reply.customer = request.user.customer
            elif hasattr(request.user, 'agent'):
                reply.agent = request.user.agent
            reply.property = property
            reply.parent_comment = parent_comment
            reply.is_reply = True
            reply.save()
            return redirect('property_single', property_id=property.id)
    else:
        form = CommentForm()
    
    context = {
        'form': form,
        'property': property,
        'parent_comment': parent_comment
    }
    return render(request, 'property/reply_to_comment.html', context)


# @login_required
# def reply_to_comment(request, comment_id):
#     parent_comment = get_object_or_404(Comment, id=comment_id)
#     property = parent_comment.property

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             reply = form.save(commit=False)
#             if hasattr(request.user, 'customer'):
#                 reply.customer = request.user.customer
#             elif hasattr(request.user, 'agent'):
#                 reply.agent = request.user.agent
#             reply.property = property
#             reply.parent_comment = parent_comment
#             reply.is_reply = True
#             reply.save()
#             return redirect('property_single', property_id=property.id)
#     else:
#         form = CommentForm()
    
#     context = {
#         'form': form,
#         'property': property,
#         'parent_comment': parent_comment
#     }
#     return render(request, 'property/reply_to_comment.html', context)




@login_required(login_url='login')
def edit_property(request, id):
    prop = Property.objects.get(id=id)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prop.img) > 0:
                os.remove(prop.img.path)
            prop.img = request.FILES['image_property']
        prop.title = request.POST.get('property')
        prop.property_type = request.POST.get('propertyType')
        prop.location = request.POST.get('location_property')
        prop.details = request.POST.get('description')
        prop.price = request.POST.get('price_property')
        prop.room_number = request.POST.get('room_property')
        prop.hall_room = request.POST.get('hall_property')
        prop.bathrooms = request.POST.get('bathroom_property')
        prop.floor = request.POST.get('floor_property')
        prop.street_number = request.POST.get('street_property')
        prop.build_year = request.POST.get('propertyAge')
        prop.house_type = request.POST.get('AccommodationType')
        prop.space = request.POST.get('space')
        prop.pool = request.POST.get('pool_property')
        prop.kitchen = request.POST.get('kitchen_property')
        prop.roof = request.POST.get('Roof_property')
        prop.modern = request.POST.get('new_property')
        prop.appendix = request.POST.get('yard_property')
        prop.elevator = request.POST.get('elevator_property')
        prop.basement = request.POST.get('basement_property')
        prop.furnished = request.POST.get('Furnished_property')
        prop.save()
        messages.success(request, "تم تعديل العقار بنجاح!")
        return redirect('property_grid')
    context = {'prop': prop}
    return render(request, 'property/edit_property.html', context)


@login_required(login_url='login')
def delete_property(request, id):
    prop = Property.objects.get(id=id)
    if request.method == "POST":
        if len(prop.img) > 0:
            os.remove(prop.img.path)
        prop.delete()
        messages.success(request, "تم حذف العقار بنجاح!")
        return redirect('property_grid')
    context = {'prop': prop}
    return render(request, 'property/delete_property.html', context)


@login_required(login_url='login')
def my_property(request, id):
    agt = Agent.objects.get(id=id)
    properties = agt.properties.all()
    num_properties = properties.count()
    context = {
        'agt': agt,
        'properties': properties,
        'num_properties': num_properties
    }
    return render(request, 'property/my_property.html', context)
