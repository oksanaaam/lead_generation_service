from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LeadGeneratorForm, SignupForm


def login_view(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("interface:lead_generator")
            else:
                print("Invalid credentials")

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "registration/logged_out.html")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("interface:lead_generator")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def lead_generator_view(request):
    form = LeadGeneratorForm()

    if request.method == "POST":
        form = LeadGeneratorForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data["keywords"]
            location = form.cleaned_data["location"]
            leads_num = form.cleaned_data["leads_num"]

            return redirect("interface:lead_generator")

    return render(request, "interface/lead_generator.html", {"form": form})


def deploying_page(request):
    return render(request, "interface/deploying_page.html")
