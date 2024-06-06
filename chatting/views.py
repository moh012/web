from django.shortcuts import render, redirect, get_object_or_404
from chatting.models import Contact, Report_Customer, Report_Agent
from accounts.models import Customer
from property.models import Property
from order.models import Order
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def about(request):
    return render(request, 'chatting/about.html')


def blog_grid(request):
    return render(request, 'chatting/blog_grid.html')


def blog_single(request):

    return render(request, 'chatting/blog_single.html')


def chat(request):

    return render(request, 'chatting/chat.html')


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(username=username,
                       email=email,
                       subject=subject,
                       message=message)
        data.save()

    return render(request, 'chatting/contact.html')


@login_required(login_url='login')
def report_property(request, id_property):
    prop = Property.objects.get(id=id_property)
    if request.method == "POST":
        rprtcust = Report_Customer.objects.create(
            property=prop,
            customer=request.user.customer,
            report_type=request.POST.get('report_type'),
            report_state=request.POST.get('report_status'),
            report_text=request.POST.get('report_text'))
        rprtcust.save()
        messages.error(request, "تم الإبلاغ عن العقار!")
        return redirect('property_grid')
    return render(request, 'chatting/report_property.html')


@login_required(login_url='login')
def report_order(request, id_order):
    ord = Order.objects.get(id=id_order)
    if request.method == "POST":
        rprtagnt = Report_Agent.objects.create(
            order=ord,
            agent=request.user.agent,
            report_type=request.POST.get('report_type'),
            report_state=request.POST.get('report_status'),
            report_text=request.POST.get('report_text'))
        rprtagnt.save()
        messages.error(request, "تم الإبلاغ عن الطلب!")
        return redirect('order_grid')
    return render(request, 'chatting/report_order.html')
