from .models import *
from .forms import *
from django.shortcuts import redirect, render


#Create here
def site_rate(request, pk):
    post = Site.objects.get(pk=pk)
    current_user_id = request.user.id
    user_profile = UserProfile.objects.get(user_id=current_user_id)

    if request.user.is_authenticated:

        if request.method == 'POST':
            form = RatingsForm(request.POST)
            if form.is_valid():
                # 'design', 'usability', 'content', 'creativity'
                rate = Rate()
                rate.design = form.cleaned_data.get('design')
                rate.usability = form.cleaned_data.get('usability')
                rate.content = form.cleaned_data.get('content')
                rate.creativity = form.cleaned_data.get('creativity')


                design = rate.aggregate(Avg('design'))['design__avg']
                usability = rate.aggregate(Avg('usability'))['usability__avg']
                content = rate.aggregate(Avg('content'))['content__avg']
                creativity = rate.aggregate(Avg('creativity'))['creativity__avg']
                average = rate.aggregate(Avg('average'))['average__avg']
                rate = form.save(commit=False)
                rate.average = (rate.design + rate.usability + rate.content + rate.creativity) / 4
                # print(rate.average)
                rate.post = post
                rate.user = user
                rate.save()
            return redirect('site', post)
        else:
            form = RatingsForm()
        return render(request, 'site.html', {'post': post, 'rate': rate, 'rating_form': form, 'design': design, 'usability': usability, 'content': content,'creativity':creativity, 'average':average})