from django.shortcuts import render
from chatting.models import Comment
from accounts.models import Customer
from django.contrib.auth.models import User

# Create your views here.


def property(request):
    return render(request, 'property/property.html')


def property_grid(request):
    return render(request, 'property/property_grid.html')


def property_single(request):

    if request.method == 'POST':
        customer = Customer(id=1)
        comment = request.POST.get('message')
        data = Comment(customer=customer, comment=comment)
        data.save()

    context = {
        'cuscomment': Comment.objects.all(),
        'commentnum': Comment.objects.all().count(),
        'cust': Customer.objects.all(),
    }

    return render(request, 'property/property_single.html', context)
