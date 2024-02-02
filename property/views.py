from django.shortcuts import render


# Create your views here.

def property(request):
    return render(request, 'property/property.html')


def property_grid(request):
    return render(request, 'property/property_grid.html')


def property_single(request):
    return render(request, 'property/property_single.html')


