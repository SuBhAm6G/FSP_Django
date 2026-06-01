from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.base_fun),
    path("home/", views.home_fun),
    path("contact/", views.contact_fun),
    path("about/", views.about_fun),
]