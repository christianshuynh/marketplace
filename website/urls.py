from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("forsale", views.forsale, name="forsale"),
    path("list", views.listanitem, name="listanitem")
]