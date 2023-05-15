from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    context = {"short_url": None}
    return render(request, "shortener/index.html", context)


def shorten(request: HttpRequest):
    # TODO
    return HttpResponse("shorten-response")
