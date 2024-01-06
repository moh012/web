from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def createAccount(request):
    return render(request, 'pages/createAccount.html')

def logIn(request):
    return render(request, 'pages/logIn.html')

def phoneNumber(request):
    return render(request, 'pages/phoneNumber.html')

def verificationCode(request):
    return render(request, 'pages/verificationCode.html')