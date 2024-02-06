from django.shortcuts import render
from chatting.models import Contact, Comment
from accounts.models import Customer


def about(request):
    return render(request, 'chatting/about.html')


def blog_grid(request):
    return render(request, 'chatting/blog_grid.html')


def blog_single(request):

    return render(request, 'chatting/blog_single.html')


def chat(request):

    return render(request, 'chatting/chat.html')


def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(username=username,
                       email=email,
                       subject=subject,
                       message=message)
        data.save()

    return render(request, 'chatting/contact.html')
