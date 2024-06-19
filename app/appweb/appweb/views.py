# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("E4 validé, bouya !")

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
