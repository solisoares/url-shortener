from typing import Union

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def index(request: HttpRequest, short_url: Union[str, None] = None):
    return render(request, "shortener/index.html")


def shorten(request: HttpRequest):
    # TODO
    # - colect original url
    # - generate shortened url
    # - save to database
    # - redirect to shortened view with shortened url as arg

    # STUB
    shortened_url = "SHORTENED URL"
    return HttpResponseRedirect(reverse("shortener:shortened", args=(shortened_url,)))


def shortened(request: HttpRequest, shortened_url: Union[str, None]):
    # TODO
    # - get shortened and original url from database
    # - render the shortened page with original and shortened url as context

    # STUB
    original_url = "ORIGINAL URL"
    context = {"original_url": original_url, "shortened_url": shortened_url}
    return render(request, "shortener/shortened.html", context)
