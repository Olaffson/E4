from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def status_view(request):
    return HttpResponse("L'application est en ligne")
