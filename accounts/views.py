from django.shortcuts import render

from django.template import loader  #اضافتي للمستقبل القريب

from property.models import *


def agent_single(request):
    return render(request, 'accounts/agent_single.html')


def agents_grid(request):
    return render(request, 'accounts/agents_grid.html')


def login(request):
    return render(request, 'accounts/login.html')


def privacy_policy(request):
    return render(request, 'accounts/privacy_policy.html')


def signup(request):
    return render(request, 'accounts/signup.html')


def userdata(request):
    return render(request, 'accounts/userdata.html')


def verification(request):
    return render(request, 'accounts/verification.html')
