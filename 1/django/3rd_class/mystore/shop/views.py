from multiprocessing import context
from django.shortcuts import render

# Create your views here.

info = {
    "Name": "Afif",
    "Adress": "Kuwait",
    "Phone": "2348888"
}


def index(request):
    return render(request, "index.html", context=info)


def about(request):
    return render(request, "about.html")
