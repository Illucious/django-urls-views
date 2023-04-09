from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def challenges_main(request):
    return HttpResponse("This is the main page for challenges.")


def january_challenge(request):
    return HttpResponse("This is the response for the january challenge.")


def february_challenge(request):
    return HttpResponse("This is the response for the february challenge.")
