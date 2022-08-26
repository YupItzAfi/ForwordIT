from django.shortcuts import render
from .forms import ProfileForm
from django.contrib import messages
from .models import UserProfile


# Create your views here.


def index(request):
    profile = UserProfile.objects.all()

    context = {
        "profile": profile,
    }

    return render(request, "index.html", context=context)


def create_profile(request):
    forms = ProfileForm()

    if request.method == "POST":
        forms = ProfileForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            messages.success(request, "profile created successfully")
        else:
            messages.success(request, "profile is not created successfully")

    context = {
        "forms": forms,
    }

    return render(request, "profile.html", context=context)
