from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def shopHome(request):
    return HttpResponse("hey there")