# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("E4 validé, bouya !")

from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


def home(request):
    return render(request, 'home.html')


class CustomLoginView(LoginView):
    template_name = 'login.html'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
