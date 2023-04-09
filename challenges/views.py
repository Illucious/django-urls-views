from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def challenges_main(request):
    return HttpResponse("This is the main page for challenges.")

"""
def january_challenge(request):
    return HttpResponse("This is the response for the january challenge.")


def february_challenge(request):
    return HttpResponse("This is the response for the february challenge.")
"""
#dynamic view
def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "This is the response for the january challenge."
    elif month == "february":
        challenge_text = "This is the response for the february challenge."
    elif month == "march":
        challenge_text = "This is the response for the march challenge."
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)