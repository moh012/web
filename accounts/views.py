from collections import UserDict
from urllib import request
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from property.models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required
import re
from django.core.files.storage import default_storage
import os


def login(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:

        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #خدمة تذكرني
            if 'rememberme' not in request.POST:
                request.session.set_expiry(0)
            auth.login(request, user)
        else:
            messages.error(request,
                           ' هناك خطأ في كلمة اسم المستخدم أو كلمة المرور')

        return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'GET':
        userNum = request.GET.get('numberInput')
    return render(request, 'accounts/signup.html', context=userNum)


def logout(request):

    if request.user.is_authenticated:
        auth.logout(request)

    return redirect('index')


def userdata(request):
    if request.method == 'POST' and 'btncreate' in request.POST:
        user_photo = None
        if len(request.FILES) != 0:
            user_photo = request.FILES.get('user_photo', None)
        username = None
        email = None
        password = None
        accepted = None
        account_type = request.POST.get('account_type', None)
        is_added = None
        usernum = request.GET.get('numberInput')

        if 'user' in request.POST: username = request.POST['user']
        else:
            messages.error(request, '   يوجد خطأ في اسم المستخدم  ')

        if 'pass' in request.POST: password = request.POST['pass']
        else:
            messages.error(request, '   يوجد خطأ في كلمة المرور  ')

        if 'email' in request.POST: email = request.POST['email']
        else:
            messages.error(request, '  يوجد خطأ في البريد الالكتروني  ')

        if 'account_type' in request.POST:
            account_type = request.POST['account_type']
        else:
            messages.error(request, '   يوجد خطأ في نوع الحساب  ')

        if 'accepted' in request.POST: accepted = request.POST['accepted']

        #التحقق من القيم
        if username and password and email and account_type:
            #الموافقة على الشروط
            if accepted == 'on':
                # التحقق من وجود المستخدم
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'مستخدم موجود ')
                else:
                    #التحقق من وجود الايميل
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'ايميل موجود')
                    else:
                        patt = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                        if re.match(patt, email):
                            #  اضافة للمستخدم في جانغو

                            user = User.objects.create_user(username=username,
                                                            password=password,
                                                            email=email)

                            #  اضافة المستخدم بالحقول الخاصة فيه في ملف المودل مع الذي أنشأناه مع جانغو

                            if account_type == 'agent':
                                Agent.objects.create(user=user,
                                                     profil_photo=user_photo,
                                                     phone=usernum)
                                messages.success(request,
                                                 'مرحبا وكيلنا العزيز ')
                                user.save()
                                return redirect('login')

                            elif account_type == 'customer':
                                Customer.objects.create(user=user,
                                                        photo=user_photo,
                                                        phone=usernum)
                                messages.success(request,
                                                 'مرحبا عميلنا العزيز ')
                                user.save()
                                return redirect('login')

                            username = ''
                            password = ''
                            email = ''
                            accepted = None
                            account_type = None
                            is_added = True

                        else:
                            messages.error(request,
                                           ' هناك خطأ في البريد الالكتروني')
            else:
                messages.error(request,
                               'يجب الموافقة على الشروط وسياسة الاستخدام  ')
        else:
            messages.error(request, 'تحقق من الحقول المدخلة')

        return render(
            request, 'accounts/userdata.html', {
                'user_photo': user_photo,
                'user': username,
                'pass': '',
                'email': email,
                'is_added': is_added
            })
    else:
        return render(request, 'accounts/userdata.html')


def agent_single(request, id):
    agt = Agent.objects.get(id=id)
    properties = agt.properties.all()
    num_properties = properties.count()
    context = {
        'agt': agt,
        'properties': properties,
        'num_properties': num_properties
    }
    return render(request, 'accounts/agent_single.html', context)


def agents_grid(request):
    if request.method == 'POST':

        return render(request, 'accounts/agents_grid.html')
    else:

        return render(request, 'accounts/agents_grid.html')


def verification(request):
    if request.method == 'POST':

        return render(request, 'accounts/verification.html')
    else:

        return render(request, 'accounts/verification.html')


def privacy_policy(request):
    return render(request, 'accounts/privacy_policy.html')


#The old Code
# @login_required
# def edit_profile(request ,id):
#     if request.method == 'POST':
#         agt = Agent.objects.get(id=id)
#         user = request.user

#         if request.POST.get('user'):
#             user.username = request.POST['user']

#         if request.POST.get('email'):
#             user.email = request.POST['email']

#         user.save()

#         messages.success(request, 'تم تحديث ملف التعريف بنجاح')

#         return redirect('edit_profile')

#     context = {
#         'user': request.user.username,
#         'email': request.user.email,
#         'agt': agt

#     }
#     return render(request, 'accounts/edit_profile.html', context)


def edit_profile(request, id):
    if request.method == 'POST' and 'btnsave' in request.POST:

        if request.user is not None and request.user.id is not None:

            agt = Agent.objects.filter(user=request.user).first()
            cust = Customer.objects.filter(user=request.user).first()

            if request.POST['user'] and ['email'] and ['first_name'] and [
                    'last_name'
            ] and ['address'] and ['who_i'] and ['facebook'] and [
                    'instagram'
            ] and ['twitter']:
                request.user.username = request.POST['user']
                request.user.email = request.POST['email']
                request.user.first_name = request.POST['first_name']
                request.user.last_name = request.POST['last_name']
                request.user.save()

                if hasattr(request.user, 'agent'):
                    request.user.agent.address = request.POST['address']
                    request.user.agent.who_i = request.POST['who_i']
                    request.user.agent.facebook = request.POST['facebook']
                    request.user.agent.instagram = request.POST['instagram']
                    request.user.agent.twitter = request.POST['twitter']
                    request.user.agent.save()

                elif hasattr(request.user, 'customer'):
                    request.user.customer.facebook = request.POST['facebook']
                    request.user.customer.instagram = request.POST['instagram']
                    request.user.customer.twitter = request.POST['twitter']
                    request.user.customer.save()

                auth.login(request, request.user)
                messages.success(request, 'تم حفظ التعديلات')
            else:
                messages.error(request, 'تحقق من القيم')

            return redirect('index')

    else:
        if request.user is not None:
            context = None
            if not request.user.is_anonymous:
                agt = Agent.objects.filter(user=request.user).first()
                cust = Customer.objects.filter(user=request.user).first()
                context = {
                    'agt': agt,
                    'cust': cust,
                    'email': request.user.email,
                }

    return render(request, 'accounts/edit_profile.html', context)