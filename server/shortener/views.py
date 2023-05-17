from django.http import HttpRequest
from django.shortcuts import render

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
                    "shortened_url": f"http://{request.get_host()}/shortener/"
                    + url_model.short_url,
                },
            )

    else:
        shortener_form = ShortenerForm()

    return render(request, "shortener/index.html", {"shortener_form": shortener_form})
