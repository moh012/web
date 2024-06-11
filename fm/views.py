from django.shortcuts import get_object_or_404, render, redirect
from .forms import fmForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from order.models import Order
from property.models import Property
from fm.models import Financial_Movement

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


@login_required(login_url='login')
def payment(request, pay_id):
    # تحقق من وجود الطلب أو العقار بناءً على نوع المستخدم
    ord = None
    prop = None
    if hasattr(request.user, 'agent'):
        prop = get_object_or_404(Property, id=pay_id)
    elif hasattr(request.user, 'customer'):
        ord = get_object_or_404(Order, id=pay_id)
    
    if request.method == 'POST':
        fm = fmForm(request.POST, request.FILES)
        if fm.is_valid():
            financial_movement = fm.save(commit=False)
            
            if hasattr(request.user, 'agent'):
                financial_movement.agent = request.user.agent
                financial_movement.property = prop
            elif hasattr(request.user, 'customer'):
                financial_movement.customer = request.user.customer
                financial_movement.order = ord

            financial_movement.save()
            messages.success(request, 'تم إرسال البيانات بنجاح سيتم التحقق من قبل إدارة الموقع.')
        else:
            messages.error(request, 'حدث خطأ أثناء إرسال البيانات. يرجى التحقق من الحقول.')
    else:
        fm = fmForm()

    context = {
        'fm': fm,
    }

    # أضف الطلب أو العقار إلى السياق إذا كانت موجودة
    if ord:
        context['ord'] = ord
    if prop:
        context['prop'] = prop

    return render(request, 'fm/payment.html', context)

