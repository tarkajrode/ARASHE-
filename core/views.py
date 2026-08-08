from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def telegram(request):
    return render(request, "telegram.html")


def site_policy(request):
    return render(request, "policy.html")
