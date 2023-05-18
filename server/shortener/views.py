from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import ShortenerForm
from .models import URL


# Create your views here.
def index(request: HttpRequest):
    if request.method == "POST":
        shortener_form = ShortenerForm(request.POST)

        if shortener_form.is_valid():
            original_url: str = shortener_form.cleaned_data["original_url"]
            url_model = URL(original_url=original_url)
            url_model.save()
            return render(
                request,
                "shortener/index.html",
                {
                    "shortener_form": shortener_form,
                    "shortened_url": f"http://{request.get_host()}"
                    + reverse("shortener:index")
                    + url_model.short_url,
                },
            )

    else:
        shortener_form = ShortenerForm()

    return render(request, "shortener/index.html", {"shortener_form": shortener_form})


def redirect_hash_url(request: HttpRequest, hash):
    url_model = URL.objects.get(short_url=hash)
    url_model.update_access_count()
    return HttpResponseRedirect(url_model.original_url)
