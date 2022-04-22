from http.client import HTTPResponse
from django.views import View
from django.shortcuts import render

# Create your views here.

def user(request):
    response = '''<h1> Hello!!! </h1>'''
    return HTTPResponse(response)
