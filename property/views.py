from django.shortcuts import render, redirect, get_object_or_404
from chatting.models import Comment
from chatting.forms import CommentForm
from accounts.models import Customer, Agent
from django.contrib.auth.models import User
from property.models import Area, Property, Favorite, City, Photo_Property, Comparison
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os

# Create your views here.


def comparison(request):
    context = {
        'comp':
        Comparison.objects.all(),
        'countComp':
        Comparison.objects.filter(customer=request.user.customer).count()
    }
    return render(request, 'property/comparison.html', context)


def add_comp(request, id_property):
    try:
        property_obj = get_object_or_404(Property, id=id_property)
        user_comparisons = Comparison.objects.filter(
            customer=request.user.customer)
        if user_comparisons.count() >= 3:
            messages.warning(
                request,
                "لقد أضفت بالفعل 3 عقارات للمقارنة. يرجى إزالة واحد قبل إضافة واحد جديد."
            )
            return redirect('comparison')
        fave, created = Comparison.objects.get_or_create(
            property=property_obj, customer=request.user.customer)
        if created:
            messages.success(request, "تم إضافة العقار إلى المقارنة!")
        else:
            messages.info(request, "العقار موجود بالفعل في المقارنة!")
    except Exception as e:
        messages.error(request, f"حدث خطأ: {e}")
    return redirect('comparison')


def rm_comp(request, id):
    comp = Comparison.objects.filter(id=id)
    comp.delete()
    messages.error(request, "تم إزالة العقار من المقارنة!")
    return redirect('comparison')


@login_required(login_url='login')
def property(request):

    context = {
        'city': City.objects.all(),
        'area': Area.objects.all(),
    }

    prop = Property()

    if request.method == 'POST':
        prop.agent = request.user.agent
        if len(request.FILES) != 0:
            prop.img = request.FILES['image_property']
        prop.title = request.POST.get('property')
        prop.property_type = request.POST.get('propertyType')
        prop.area = Area(id=request.POST.get('area'))
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
        files = request.FILES.getlist('files')
        for file in files:
            new_file = Photo_Property(
                property=prop,
                photo=file,
            )
            new_file.save()
        messages.success(request, "تم إضافة العقار بنجاح!")
        return redirect('property_grid')

    return render(request, 'property/property.html', context)


def property_grid(request):
    try:
        search = Property.objects.all()
        title = None
        property_type = None
        search_room = None
        search_bathroom = None
        if 'search_name' and 'search_type' and 'search_bathroom' in request.GET:
            title = request.GET['search_name']
            property_type = request.GET['search_type']
            search_room = request.GET['search_room']
            search_bathroom = request.GET['search_bathroom']
            if title or property_type or search_room or search_bathroom:
                search = search.filter(
                    title__icontains=title,
                    property_type__icontains=property_type,
                    room_number__icontains=search_room,
                    bathrooms__icontains=search_bathroom,
                )
    except Exception as e:
        messages.error(request, f"حدث خطأ: {e}")

    context = {
        'properties': search,
        'fave': Favorite.objects.all(),
    }
    return render(request, 'property/property_grid.html', context)


@login_required(login_url='login')
def property_single(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    comments = property.comments.filter(parent_comment__isnull=True)
    photos = list(
        Photo_Property.objects.filter(property=property)) + [property.img]

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
        'form': form,
        'photos': photos,
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
        'parent_comment': parent_comment,
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
    photo = Photo_Property.objects.filter(property=prop)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prop.img) > 0:
                os.remove(prop.img.path)
            prop.img = request.FILES['image_property']
        prop.title = request.POST.get('property')
        prop.property_type = request.POST.get('propertyType')
        prop.area = Area(id=request.POST.get('area'))
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
        messages.warning(request, "تم تعديل العقار بنجاح!")
        return redirect('property_grid')
    context = {
        'prop': prop,
        'photo': photo,
        'city': City.objects.all(),
        'area': Area.objects.all(),
    }
    return render(request, 'property/edit_property.html', context)


@login_required(login_url='login')
def delete_property(request, id):
    prop = Property.objects.get(id=id)
    if request.method == "POST":
        if len(prop.img) > 0:
            os.remove(prop.img.path)
        prop.delete()
        messages.error(request, "تم حذف العقار بنجاح!")
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
