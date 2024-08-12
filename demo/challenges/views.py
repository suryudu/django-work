from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_descriptions = {
    "january": "hurray it's time to celebrate Makar Sankranti",
    "february": "This month is special for lovers",
    "march": "Ohm namah shivvaya",
    "april": "telugu new year starts",
    "may": "Hot month of the year",
    "june": "mid of the year",
    "july": "Most excited month in the year",
    "august": "Independence month",
    "september": "vinayaka chavithi",
    "october": "amazon sales",
    "november": "no nut november",
    "december": None
}


# Create your views here.

# def index(request):
#     return HttpResponse("It's working")
#
#
# def february(request):
#     return HttpResponse("It's february and working")

def index(request):
    # list_items = ""
    months = list(monthly_descriptions.keys())
    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # return HttpResponse(f"<ul>{list_items}</ul>")
    # month_path = reverse("month-challenge")
    return render(request,"challenges/index.html",{"months":months,"ll":"ll"})


def monthly_challenge_number(request, month):
    months = list(monthly_descriptions.keys())
    if month > 12:
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    redirect_path = reverse("month-challenge", args=[months[month - 1]])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_descriptions[month]
        #     return HttpResponse(f"<h1>{monthly_descriptions[month]}</h1>")
        #     return HttpResponse(render_to_string("challenges/month_challenge.html"))
        return render(request, "challenges/month_challenge.html", {"text": challenge_text,"month":month})
    except:
        return HttpResponseNotFound("<h1>No month matched<h1>")
