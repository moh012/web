from django.shortcuts import render


def fave(request):
    return render(request, 'order/fave.html')


