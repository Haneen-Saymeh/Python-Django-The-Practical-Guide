from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# from django.shortcuts import HttpResponse
monthly_challenges={
    "jan" :"do sth in jan",
    "feb" : "do sth in feb",
    "march":"do sth in march",
    "april":"do sth in april",
    "may":"do sth in may",
    "june":"do sth in june",
    "july":"do sth in july",
    "aug":"do sth in aug",
    "sep":None
}
# def index(requst):
#     return HttpResponse("this works!") 

def feb(requst):
    return HttpResponse("this works again!") 

# def month(requst, month):
#     if month == "jan":
#         text = "eat no meat for some time"
#     elif month == 'feb':
#         text= "do something"
#     else:
#         return HttpResponseNotFound("this month is not valid")

#     return HttpResponse(text) 

# def monthNumber(request, month):
#     return HttpResponse(month)

# def month(request, month):
#     try:
#         text = monthly_challenges[month]
#     except:
#         return HttpResponseNotFound("This month not found")

#     return HttpResponse(text)

# def monthNumber(request, month):
#     months = list(monthly_challenges.keys())
#     if month > len(months):
#         return HttpResponseNotFound("this month is not found")
#     redirect_month= months[month-1]
#     return HttpResponseRedirect("/challenges/" + redirect_month)

def monthNumber(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("this month is not found")
    redirect_month= months[month-1]
    redirect_path = reverse("haneen", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def month(request, month):
    try:
        text = monthly_challenges[month]
        response = f"<h1>{text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This month not found</h1>")

    return HttpResponse(response)

def allMonths(request):
    list_items=""
    months = list(monthly_challenges.keys())
    for month in months:
        month_cap = month.capitalize()
        month_path= reverse("haneen", args=[month])
        list_items += f"<li><a href='{month_path}'>{month_cap}</a></li>"
    response_months = f"<ul>{list_items}</ul>"

    return HttpResponse(response_months)

def index(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/index.html", {
        "text" : text,
        "month_name": month

    })
    except:
        raise Http404() 
        # need to make the debug to false in the setting before deployment
        # response_fail=render_to_string("404.html")
        # return HttpResponseNotFound(response_fail)

def mainpage(request):
    months= list(monthly_challenges.keys())
    return render(request,"challenges/dash.html", {
        "months":months
     })

# def index2(request):
    
#     return render(request, "challenges/index2.html")

