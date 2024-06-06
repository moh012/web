from django.shortcuts import render, redirect
from .forms import fmForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# @login_required
# def pyment(request):
#     fm= fmForm()
#     if request.method == 'POST':
#         fm = fmForm(request.POST, request.FILES)
#         if fm.is_valid():
#             fm.save()
#             return redirect('index')
#         else:
#             fm = fmForm()

#     return render(request, 'fm/pyment.html', {'fm': fm})

    
# شغال حلاوة ولكن دن حقول نوع المستخدم
# @login_required
# def pyment(request):
#     if request.method == 'POST':
#         fm = fmForm(request.POST, request.FILES)
#         if fm.is_valid():
#             financial_movement = fm.save(commit=False)
#             financial_movement.created_by = request.user
#             financial_movement.save()
#             messages.success(request, 'تم إرسال البيانات بنجاح.')
#             return redirect('index')
#         else:
#             messages.error(request, 'حدث خطأ أثناء إرسال البيانات. يرجى التحقق من الحقول.')
#     else:
#         fm = fmForm()
    
#     return render(request, 'fm/pyment.html', {'fm': fm})


@login_required
def payment(request):
    if request.method == 'POST':
        fm = fmForm(request.POST, request.FILES)
        if fm.is_valid():
            if request.user.is_authenticated:  
                financial_movement = fm.save(commit=False)

                if hasattr(request.user, 'agent'): 
                    financial_movement.agent = request.user.agent

                elif hasattr(request.user, 'customer'):
                    financial_movement.customer = request.user.customer

                financial_movement.save()
                messages.success(request, 'تم إرسال البيانات بنجاح.')
                return redirect('payment')
            else:
                messages.error(request, 'يجب تسجيل الدخول لإرسال البيانات.')
        else:
            messages.error(request, 'حدث خطأ أثناء إرسال البيانات. يرجى التحقق من الحقول.')
    else:
        fm = fmForm()
    
    return render(request, 'fm/payment.html', {'fm': fm})
