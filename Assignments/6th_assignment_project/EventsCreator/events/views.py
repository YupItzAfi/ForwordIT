from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Event, User
# Create your views here.


@login_required(login_url="/login")
def home(request):
    event = Event.objects.all()
    user = User.objects.all()

    context = {
        "event": event,
        "user": user,
    }

    return render(request, 'index.html', context=context)


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "User or Password is either incorrect")
            return render(request, "login.html")
    return render(request, 'login.html')


@login_required(login_url="/login")
def logout(request):
    logout(request)


def registration(request):
    return render(request, 'registration.html')


@login_required(login_url="/login")
def add_events(request):
    return render(request, 'create-events.html')


@login_required(login_url="/login")
def ticket_booking(request):
    return render(request, 'ticket_booking.html')
