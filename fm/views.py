from django.shortcuts import render


# Create your views here.
def fave(request):
    return render(request, 'order/fave.html')
