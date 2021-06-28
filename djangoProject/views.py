from django.http import HttpRequest, HttpResponseRedirect, HttpResponse


def index(request:HttpRequest):
    return HttpResponse('Welcome to Django Index Page')