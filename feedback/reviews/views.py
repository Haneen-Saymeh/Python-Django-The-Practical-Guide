from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.

def review(request):
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review= Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
            review.save()
            # print(form.cleaned_data)
            return HttpResponseRedirect("/thx")
    else:
        form = ReviewForm()
    return render(request,"rev/rev.html", {"form":form})

def thank_you(request):
    return render(request,"rev/thank.html")