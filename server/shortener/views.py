from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from shortener.forms import ShortenerForm
from shortener.models import URL


@require_http_methods(["GET", "POST"])
def index(request: HttpRequest):
    if request.method == "POST":
        shortener_form = ShortenerForm(request.POST)

        if shortener_form.is_valid():
            original_url: str = shortener_form.cleaned_data["original_url"]
            url_model, _ = URL.objects.get_or_create(original_url=original_url)
            return render(
                request,
                "shortener/index.html",
                {
                    "shortener_form": shortener_form,
                    "shortened_url": f"http://{request.get_host()}"
                    + reverse(
                        "shortener:redirect_hash_url", args=[url_model.short_url]
                    ),
                },
            )

    else:
        shortener_form = ShortenerForm()

    return render(request, "shortener/index.html", {"shortener_form": shortener_form})


@require_http_methods(["GET"])
def redirect_hash_url(request: HttpRequest, hash):
    try:
        url_model = URL.objects.get(short_url=hash)
        url_model.update_last_access()
        redirect_to = url_model.original_url
    except ObjectDoesNotExist:
        messages.warning(
            request, f'The short url you provided, "{hash}", does not exist.'
        )
        redirect_to = reverse("shortener:index")
    return HttpResponseRedirect(redirect_to)
