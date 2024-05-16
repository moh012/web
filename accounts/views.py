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
        #  messages.success(request,'قمت بتسجيل الدخول')
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


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST' and 'btnprof' in request.POST:
        # متغيرات لحقول profil  من الخاصية name
        # user_photo = None
        fname = None
        last_name = None
        password = None
        password_confirm = password
        email = None
        phone = None
        username = None
        terms = None
        is_add = None

        # if request.FILES.get('profil_photo'):
        #    profil_photo = request.FILES['profil_photo']
        #    agent = Agent.objects.create(user=request.user, profil_photo=profil_photo)
        # else:
        #    messages.error(request, 'يوجد خطأ في الصورة ')

        # حفظ صورة الملف الشخصي في قاعدة البيانات
        # جلب القيم من الفورم
        # if 'user_photo' in request.POST:
        #     user_photo = request.POST['user_photo']
        # else:
        #     messages.error(request, 'يوجد خطأ في الصورة ')

        if 'fname' in request.POST:
            fname = request.POST['fname']
        else:
            messages.error(request, 'يوجد خطأ في الاسم الأول')

        if 'last_name' in request.POST:
            last_name = request.POST['last_name']
        else:
            messages.error(request, 'يوجد خطأ في الاسم الأخير')

        if 'password' in request.POST:
            password = request.POST['password']
        else:
            messages.error(request, 'يوجد خطأ في كلمة المرور')

        if 'password_confirm' in request.POST:
            password_confirm = request.POST['password_confirm']
        else:
            messages.error(request, 'يوجد خطأ في تأكيد كلمة المرور')

        if 'phone' in request.POST:
            phone = request.POST['phone']
        else:
            messages.error(request, 'يوجد خطأ في رقم الهاتف')

        if 'email' in request.POST:
            email = request.POST['email']
        else:
            messages.error(request, 'يوجد خطأ في البريد الإلكتروني')

        if 'username' in request.POST:
            username = request.POST['username']
        else:
            messages.error(request, 'يوجد خطأ في اسم المستخدم')

        if 'terms' in request.POST:
            terms = request.POST['terms']

        # التحقق من المتغيرات (القيم)
        if fname and last_name and password and password_confirm and phone and email and username:
            if terms == 'on':
                # التحقق من المستخدم
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'هذا المستخدم موجود مسبقاً')
                else:
                    # التحقق من الايميل
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'ايميل موجود مسبقاً')
                    else:
                        patt = "r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'"
                        if re.match(patt, email):
                            # إنشاء مستخدم
                            user = User.objects.create_user(
                                first_name=fname,
                                last_name=last_name,
                                email=email,
                                password=password,
                                username=username)
                            user.save()
                            # if ser == 'on':
                            # إنشاء بروفايل للوكيل Agent
                            agent_profile = Agent(user=user, phone=phone)
                            agent_profile.save()
                            # else:
                            #       # إنشاء بروفايل  للباحث عن عقار
                            #     customer_profile = Customer(user=user, phone=phone   )
                            #     customer_profile.save()
                            # تفريغ القيم من الحقول
                            fname = ''
                            last_name = ''
                            password = ''
                            password_confirm = ''
                            phone = ''
                            email = ''
                            username = ''
                            terms = None

                            #  للتأكد من    العملية
                            messages.success(request, 'تم انشاء الحساب بنجاح')
                            is_add = True
                        else:
                            messages.error(request,
                                           'البريد الالكتروني غير صحيح')
            else:
                messages.error(request, ' يرجى الموافقة على الشروط')
        else:
            messages.error(request, 'تحقق من الحقول المدخلة')
    # لتمربر الحقول الى الفورم
        context = {
            # 'profil_photo':profil_photo,
            'fname': fname,
            'last_name': last_name,
            'password': password,
            'password_confirm': password_confirm,
            'phone': phone,
            'email': email,
            'username': username,
            'is_add': is_add
        }

        return render(request, 'accounts/profile.html', context)

    else:
        return render(request, 'accounts/profile.html')


def userdata(request):
    if request.method == 'POST' and 'btncreate' in request.POST:
        user_photo = None
        if len(request.FILES) != 0:
            user_photo = request.FILES['user_photo']
        username = None
        email = None
        password = None
        accepted = None
        account_type = request.POST.get('account_type', None)
        is_added = None
        usernum = request.GET.get('numberInput')

        # if 'user_photo' in request.POST:
        #     user_photo = request.POST['user_photo']
        # else:
        #     messages.error(request, ' يوجد خطأ في صورة المستخدم')

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
        if username and password and email and account_type and user_photo:
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

                            # هذا الكد الصحيح
                            #  اضافة المستخدم بالحقول الخاصة فيه في ملف المودل مع الذي أنشأناه مع جانغو

                            if account_type == 'agent':
                                Agent.objects.create(user=user,
                                                     profil_photo=user_photo,
                                                     phone=usernum)
                                messages.success(request,
                                                 'مرحبا وكيلنا العزيز ')
                                user.save()
                                return redirect('userdata')

                            elif account_type == 'customer':
                                Customer.objects.create(user=user,
                                                        photo=user_photo,
                                                        phone=usernum)
                                messages.success(request,
                                                 'مرحبا عميلنا العزيز ')
                                user.save()
                                return redirect('userdata')

                        #  if 'agent'in request.POST:
                        #     agent_profile = Agent(user = user)
                        #     agent_profile.save()
                        #  elif 'customer' in request.POST:
                        #      customer_profile = Customer(user = user)
                        #      customer_profile.save()

                            user_photo = ''
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
                'pass': password,
                'email': email,
                'is_added': is_added,
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


# def edit_profile(request):
#     if request.method == 'POST' and 'btnsave' in request.POST:
#         return redirect('edit_profile')
#     else:
#         if request.user.is_anonymous: return redirect ('index')
#         if request.user is not None:

#             if request.user.is_agent:
#                  agentprofile = Agent.objects.get(pk=request.user.pk)
#             elif request.user.is_customer:
#                 customerprofile = Customer.objects.get(pk=request.user.pk)

#             context = {
#                 'user': request.user.username,
#                 'pass': request.user.password,
#                 'email': request.user.email,
#             }

#             return render(request, 'accounts/edit_profile.html', context)

#         else:
#             return render('accounts/index.html')

# Thr old Code
# def edit_profile(request):
#     if request.method == 'POST' and 'btnsave' in request.POST:
#         if request.user is not None and not request.user.id is not None:
#             agrent_profile = Agent.objects.get(user=request.user)

#             if request.POST['user'] and request.POST['pass'] and request.POST[
#                     'email']:
#                 # request.user.username = request.POST['user']
#                 # request.user.email = request.POST['email']
#                 if not request.POST['pass'].startswith('pbkdf2_sha256$'):
#                     request.user.set_password(request.POST['pass'])

#                 #حفظ
#                 request.user.save()
#                 agrent_profile.save()
#                 auth.login(request, request.user)
#                 messages.success(request, 'قمت بحفظ لتغييرات')
#             else:
#                 messages.error(request, 'تحقق من ادخال الحقول المعدلة')

#         return redirect('edit_profile')
#     else:
#         if request.user is not None:
#             context = None
#             if not request.user.is_anonymous:
#                 agrent_profile = Agent.objects.get(user=request.user)
#                 context = {
#                     'user': request.user.username,
#                     'pass': request.user.password,
#                     'email': request.user.email
#                 }
#             return render(request, 'accounts/edit_profile.html', context)
#         else:
#             return redirect('edit_profile')


def privacy_policy(request):
    return render(request, 'accounts/privacy_policy.html')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':

        if request.POST.get('user') and request.POST.get('email'):

            request.user.username = request.POST['user']
            request.user.email = request.POST['email']
            request.user.save()
            messages.success(request, 'تم تحديث الملف الشخصي بنجاح.')
            return redirect('edit_profile')
        else:
            messages.error(request, 'يرجى ملئ جميع الحقول بشكل صحيح.')

    context = {
        'user': request.user.username,
        'email': request.user.email,
        'cust': Customer.objects.all(),
        'agt': Agent.objects.all(),
    }
    return render(request, 'accounts/edit_profile.html', context)
