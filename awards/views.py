from django.shortcuts import render, redirect, get_object_or_404
from django.http  import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Avg

from rest_framework.views import APIView
from rest_framework import viewsets
from .serializer import *


# Create your views here.
def site_today(request):
    date = dt.date.today()
    site = Site.objects.all()[::-1]
    return render(request, 'all-sites/today-sites.html', {"date": date,"site":site})


def site_of_day(request):
    date = dt.date.all()
    return render(request, 'all-sites/today-sites.html', {"date": date})


def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day


def past_days_site(request,past_date):

        # Converts data from the string Url
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(site_today)

    site = Site.days_site(date)
    return render(request, 'all-sites/past-sites.html',{"date": date,"site":site})


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


@login_required(login_url='/accounts/login/')
def site(request,site_id):
    try:
        site= Site.objects.get(id = site_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-sites/site.html", {"site":site})


@login_required(login_url='/accounts/login/')
def new_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewSiteForm(request.POST, request.FILES)
        if form.is_valid():
            site = form.save(commit=False)
            site.developer = current_user
            site.save()
        return HttpResponseRedirect('/')

    else:
        form = NewSiteForm()
    
    form = NewSiteForm()
    return render(request, 'new-site.html', {"form":form})


@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = UserProfile.objects.get(user_id=user)
    sites = Site.objects.filter(profile__id=id)[::-1]
    return render(request, "websites/profile.html", context={"user":user,
                                                             "profile":profile,
                                                             "sites":sites})



def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse("siteToday"))
            else:
                return HttpResponseRedirect(reverse("user_login")) #raise error/ flash

        else:
            return HttpResponseRedirect(reverse("user_login")) #raise error/ flash
    else:
        return render(request, "auth/login.html", context={})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("siteToday"))


def register(request):
    registered = False
    

    if request.method == "POST":
        user_form = UserForm(request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = UserProfile()
            user_profile.user = user
            # user_profile.save()
            user_profile.save()
            registered = True
            

            return HttpResponseRedirect(reverse("user_login"))

        else:
            pass

    else:
        user_form = UserForm()
        

    return render(request, "auth/register.html", context={"user_form":user_form,
                                                          "registered":registered})


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=current_user_id)
    if request.method == 'POST':

        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid(): 

            user_profile.profile_pic = form.cleaned_data.get('profile_pic')
            user_profile.phone_number = form.cleaned_data.get('phone_number')
            user_profile.bio = form.cleaned_data.get('bio')

            user_profile.save()
            messages.success(request, 'Your profile has been updated.')
        return redirect(my_profile)

    else:
        form = UserProfileForm()
    return render(request, 'create-profile.html', {"form": form})



@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=current_user_id)
    
    try:
        profile = UserProfile.objects.get(user_id=current_user_id)
    except UserProfile.DoesNotExist:
        return redirect(create_profile)
    site = Site.objects.filter(developer_id=current_user_id)
    

    return render(request, 'my-profile.html', { "site": site, "user_profile": user_profile},)
    
@login_required(login_url='/accounts/login/')
def site_rate(request, pk):
    site = Site.objects.get(pk=pk)
    current_user = request.user
    user = User.objects.get(username = request.user)
    # post = Site.objects.get(title = pk)
    current_user_id = request.user.id
    # user = User.objects.get(id=current_user_id)
    user_profile = UserProfile.objects.get(user_id=current_user_id)

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RatingsForm(request.POST)
            user = get_object_or_404(User, pk=current_user_id)
            if form.is_valid():
                # 'design', 'usability', 'content', 'creativity'
                rate = Rate()
                rate.design = form.cleaned_data.get('design')
                rate.usability = form.cleaned_data.get('usability')
                rate.content = form.cleaned_data.get('content')
                rate.creativity = form.cleaned_data.get('creativity')

                post_to_be_saved = Site.objects.get(pk=pk)
                rate.post= post_to_be_saved
                rating_user = User.objects.get(pk=request.user.id)
                rate.user= rating_user

                design = Rate.objects.aggregate(Avg('design'))['design__avg']
                usability = Rate.objects.aggregate(Avg('usability'))['usability__avg']
                content = Rate.objects.aggregate(Avg('content'))['content__avg']
                creativity = Rate.objects.aggregate(Avg('creativity'))['creativity__avg']
                average = Rate.objects.aggregate(Avg('average'))['average__avg']
                # rate = form.save(commit=False)
                rate.average = (rate.design + rate.usability + rate.content + rate.creativity) / 4
                print(rate.average)
               
                if request.user.is_authenticated:    
                   user_id = request.user.id           
                   has_voted = Rate.objects.all().filter(post_id=site.id,user_id=user_id)
                   if has_voted:                
                        messages.error(request,'You have already voted for this post')                
                        return redirect('site_rate', site.id)                                    
               
                rate.save_rate()
            return redirect('site_rate', site.id)
        else:
            form = RatingsForm()
        
        rate = Rate.objects.filter(post_id=site.id)
        total_rates= Rate.objects.filter(post_id=site.id).count()

        context = {
            'site':site, 
            'rating_form': form,
            'rate':rate,
            'total_rates': total_rates
            
        }
        return render(request, 'all-sites/site.html', context)

    return render(request,'all-sites/today-sites.html')

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
   
    
class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer    