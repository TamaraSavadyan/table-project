from django.http import HttpResponse
from django.shortcuts import render


def user(request):
    return HttpResponse("Hello!!!!")

def home(request):
    return render(request, "table/home.html", {})
