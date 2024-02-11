from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from property.models import *
from accounts.models import *
import re



def login(request):
    if request.method == 'POST'  and 'btnlogin' in request.POST:
            
            username = request.POST['user']
            password = request.POST['pass']

            agent = auth.authenticate(username =username , password =password )

            if agent is not None:
                 auth.login(request,agent)
                 messages.success(request,'قمت بتسجيل الدخول')
            else:
                 messages.error(request,' هناك خطأ في كلمة اسم المستخدم أو كلمة المرور')
                 
            return redirect('login')
    else:
         return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST' and 'btnsignup' in request.POST:
            
            messages.info(request , 'This is POST')
            
            messages.success(request, 'tHIS IS btn signup')
            return redirect('signup')
    else:

        return render(request, 'accounts/signup.html')


def profile(request):
    if request.method == 'POST' and 'btnprof' in request.POST:
        # متغيرات لحقول profil  من الخاصية name
        # profil_photo = None
        fname = None
        last_name = None
        password = None
        password_confirm=password
        email = None
        phone = None
        username = None
        terms = None
        is_add= None
        ser = None
        


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
        if  fname and last_name and password and password_confirm and phone and email and username:
            if terms == 'on':
                # التحقق من المستخدم
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'هذا المستخدم موجود مسبقاً')
                else:
                    # التحقق من الايميل
                    if User.objects.filter(email=email).exists():
                        messages.error(request, 'ايميل موجود مسبقاً')
                    else:
                        patt = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                        if re.match(patt, email):
                            # إنشاء مستخدم
                            user = User.objects.create_user(first_name=fname, last_name=last_name,
                                                            email=email, password=password, username=username)
                            user.save()
                                
                            if ser == 'on':

                                # إنشاء بروفايل للوكيل Agent
                                agent_profile = Agent(user=user, phone=phone   )
                                agent_profile.save()
                            else:
                                  # إنشاء بروفايل  للباحث عن عقار
                                customer_profile = Customer(user=user, phone=phone   )
                                customer_profile.save()
                            # تفريغ القيم من الحقول

                            fname = ''
                            last_name = ''
                            password = ''
                            password_confirm =''
                            phone =''
                            email = ''
                            username = ''
                            terms = None
                            ser = None

                            #  للتأكد من العملية
                            messages.success(request, 'تم انشاء الحساب بنجاح')
                            is_add =True
                        else:
                            messages.error(request, 'البريد الالكتروني غير صحيح')
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
            'password_confirm' :password_confirm,
            'phone': phone,
            'email': email,
            'username': username,
            'is_add' :is_add
        }

        return render(request, 'accounts/profile.html', context)
    else:
        return render(request, 'accounts/profile.html')

def agent_single(request):
    if request.method == 'POST':
            
            messages.info(request , 'This is POST')
            return redirect('agent_single')
    else:

        return render(request, 'accounts/agent_single.html')



def agents_grid(request):
    if request.method == 'POST':
            
            messages.info(request , 'This is POST')
            return redirect('agent_single')
    else:

        return render(request, 'accounts/agents_grid.html')


def userdata(request):
    if request.method == 'POST':
            
            messages.info(request , 'This is POST')
            return redirect('userdata')
    else:

        return render(request, 'accounts/userdata.html')

def verification(request):
    if request.method == 'POST':
            
            messages.info(request , 'This is POST')
            return redirect('verification')
    else:

        return render(request, 'accounts/verification.html')

def edit_profile(request):
    if request.method == 'POST':
            
            messages.info(request , 'This is POST')
            return redirect('edit_profile')
    else:

        return render(request, 'accounts/edit_profile.html')



def privacy_policy(request):
    return render(request, 'accounts/privacy_policy.html')
