from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

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
def monthly_challengeby_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/"+redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month is not yet supported")
    return HttpResponse(challenge_text)