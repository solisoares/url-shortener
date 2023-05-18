from django.urls import path

from shortener import views


app_name = "shortener"  # app namespace

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:hash>", views.redirect_hash_url, name="redirect_hash_url"),
]
