from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

# Create your views here.
def home_fun(request):
    return render(request, "home.html")

def contact_fun(request):
    return render(request, "contact.html")

def about_fun(request):
    return render(request, "about.html")

def base_fun(request):
    return render(request, "base.html")

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomerForm()
    return render(request, "add_customer.html", {'form': form})