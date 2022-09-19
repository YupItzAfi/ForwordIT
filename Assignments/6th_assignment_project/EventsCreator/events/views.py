from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Event, User, Categorie
from .forms import *
from .decorators import *
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


def log_in(request):
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
def log_out(request):
    logout(request)


@unauthenticated_user
def registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            login(request, user)
        return redirect('home')
    context = {
        "form": form
    }
    return render(request, 'registration.html', context=context)


@login_required(login_url="/login")
def add_events(request):
    category = Categorie.objects.all()
    event = Event
    context = {
        "category": category,
        "event": event.objects.all(),
    }
    return render(request, 'create-events.html', context=context)


@login_required(login_url="/login")
def ticket_booking(request):
    return render(request, 'ticket_booking.html')
