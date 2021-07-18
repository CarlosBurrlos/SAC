from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponseBadRequest
from .MainHandlers.Handlers import loginHandler


# Create your views here.
def login(request: HttpRequest):

    if request.method == 'GET':
        return render(request, 'main/login.html')

    requestContent = request.POST

    try:
        loginHandler(requestContent)
    except Exception:
        # TODO :: Log this exception and return a bad request

        return HttpResponseBadRequest

    return redirect('home/')

def home(request: HttpRequest):
    return render(request, 'main/index.html')
