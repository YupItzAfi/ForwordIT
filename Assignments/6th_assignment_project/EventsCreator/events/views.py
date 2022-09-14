from django.shortcuts import render  # , redirect


# Create your views here.


@login_required()
def home(request):
    return render(request, 'index.html')


def login(request):

    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')
