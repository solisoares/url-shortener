from django.http import HttpRequest
from django.shortcuts import render

from .forms import ShortenerForm


# Create your views here.
def index(request: HttpRequest):
    if request.method == "POST":
        # TODO
        # - colect original url
        # - generate shortened url
        # - save to database

        shortener_form = ShortenerForm(request.POST)

        # STUB -------------------------
        shortened_url = "SHORTENED URL"
        # ------------------------------

        return render(
            request,
            "shortener/index.html",
            {"shortener_form": shortener_form, "shortened_url": shortened_url},
        )

    else:
        shortener_form = ShortenerForm()
        return render(
            request, "shortener/index.html", {"shortener_form": shortener_form}
        )
