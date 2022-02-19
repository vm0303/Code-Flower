from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# for testing
from django.http import HttpResponse


def home(request):
    return render(request, 'main/home.html')

def topics(request):
    return render(request, 'main/topics.html')