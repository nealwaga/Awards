from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as  dt
from django.contrib.auth.decorators import login_required


# Create your views here.
def site_today(request):
    date = dt.date.today()
    return render (request, 'all-sites/today-sites.html', {'date':date})


def site_of_day(request):
    date = dt.date.all()
    return render(request, 'all-sites/today-sites.html', {'date': date})


#A func that get the weekday number for the date
def convert_dates(dates):
    day_number = dt.date.weekday(dates)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    #Return the actual day of the week
    day = days[day_number]
    return day


def past_days_site(request, past_date):
    #Converts data from the string Url
    try:
        #Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(site_of_day)

    return render(request, 'all-sites/past-sites.html', {"date": date}) 


@login_required(login_url='/accounts/login/')
def search_results(request): 
    
    if 'site' in request.GET and request.GET["site"]:
        search_term = request.GET.get("site")
        searched_websites = Site.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-sites/search.html',{"message":message,"websites": searched_websites})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-sites/search.html',{"message":message})
