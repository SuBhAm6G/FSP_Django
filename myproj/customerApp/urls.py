from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.base_fun),
    path("home/", views.home_fun, name="home"),
    path("contact/", views.contact_fun),
    path("about/", views.about_fun),
    path("add_customer/", views.add_customer, name="add_customer"),
]
