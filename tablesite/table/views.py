from django.http import HttpResponse
from django.shortcuts import render
from .models import TableContent

def home(request):
    return render(request, "table/home.html", {})

def table(request):
    
    table_content = TableContent.objects.values()
    print(table_content)

    return render(request, "table/table.html", {"table content": table_content})
