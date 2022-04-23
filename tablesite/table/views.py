from django.http import HttpResponse
from django.shortcuts import render
from .models import TableContent

def home(request):
    return render(request, "table/home.html", {})

def table(request):
    return render(request, "table/table.html", {})

