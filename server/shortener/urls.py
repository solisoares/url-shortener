from django.urls import path

from . import views


app_name = "shortener"  # app namespace

urlpatterns = [
    path("", views.index, name="index"),
    path("shorten/", views.shorten, name="shorten"),
    path("shortened/<shortened_url>", views.shortened, name="shortened"),
]
