from django.shortcuts import render

# Create your views here.
def home_fun(request):
    return render(request, "home.html")

def contact_fun(request):
    return render(request, "contact.html")

def about_fun(request):
    return render(request, "about.html")