from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# for testing
from django.http import HttpResponse


def testing(request):
    return render(request, 'main/home.html')


def third_party_login(request):
    return HttpResponse("<h1>login-test</h1>")
