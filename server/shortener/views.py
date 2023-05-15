from typing import Union

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request: HttpRequest, short_url: Union[str, None] = None):
    return render(request, "shortener/index.html")


def shorten(request: HttpRequest):
    # TODO
    return HttpResponseRedirect(reverse("shortener:index"))
