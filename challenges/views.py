from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january":"Meditate for 5-10 Minutes a Day",
    "february":"Write down 3 things you're grateful for",
    "march":"Do at least 25 jumping jacks",
    "april":"Sit down at the table for breakfast every morning",
    "may":"Read for 15 minutes before bed each night",
    "june":"Light incense or a candle when you get home",
    "july":"Write a letter to someone every day",
    "August":"Write down one thing each day you love about yourself",
    "september":"Watch 30 minutes of that show you've been meaning to catch up on",
    "october":"Make the bed each morning first thing",
    "november":"Cook a meal for yourself each day",
    "december":"Take a walk rain or shine"
}

# Create your views here.
def index(request):
    list_items = ""
    months  = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
       
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challengeby_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not yet supported</h1>")
    