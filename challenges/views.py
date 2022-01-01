from django.http import response
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
#from django.template.loader import render_to_string

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
    "december":None
}

# Create your views here.
def index(request):
    months  = list(monthly_challenges.keys())
          
    return render(request, "challenges/index.html", {
        "months": months
    })


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
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "text_month": month
        })
    except:
        return HttpResponseNotFound("<h1>This month is not yet supported</h1>")
    