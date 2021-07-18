from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def login(request: HttpRequest):
    return render(request, 'main/login.html')

def home(request: HttpRequest):
    return render(request, 'main/index.html')