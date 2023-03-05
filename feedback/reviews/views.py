from django.shortcuts import render
from .forms import ReviewForm
from django.http import HttpResponseRedirect
from .models import *
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView



# class based view to create and submit form
# class ReviewView(View):
#     def get(self, request):
#         form=ReviewForm()
#         return render(request,"rev/rev.html",{"form":form})
    
#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return render(request, "rev/thank.html")
#         return render(request,"rev/rev.html",{"form":form})
    
# using form view to create and submit a form
# class ReviewView(FormView):
#     form_class= ReviewForm
#     template_name="rev/rev.html"
#     success_url="/reviews"
    
#     def form_valid(self, form) :
#         form.save()
#         return super().form_valid(form)
    

# using create view to create and submit a form
# There is also update and delete views
class ReviewView(CreateView):
    model=Review
    form_class=ReviewForm
    template_name="rev/rev.html"
    success_url="/reviews"
    
    




# Function based view

# def review(request):
#     if request.method=='POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review= Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'],rating=form.cleaned_data['rating'])
#             review.save()
#             # print(form.cleaned_data)
#             return HttpResponseRedirect("/thx")
#     else:
#         form = ReviewForm()
#     return render(request,"rev/rev.html", {"form":form})



class ThankYouView(TemplateView):
    template_name="rev/thank.html"



# using template view
# class ReviewsListView(TemplateView):
#     template_name="rev/list.html"

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         reviews=Review.objects.all()
#         context["reviews"]=reviews
#         return context
    
# using list view
class ReviewsListView(ListView):
    template_name="rev/list.html"
    model =Review
    context_object_name="reviews"
    def get_queryset(self):
        base_query= super().get_queryset()
        data=base_query.filter(rating__gt=4)
        return data
    

# using template view for single review 
    
# class ReviewSingleView(TemplateView):
#     template_name="rev/one.html"

#     def get_context_data(self, **kwargs):
#         context= super().get_context_data(**kwargs)
#         one_review=Review.objects.get(id=kwargs["id"])
#         context["one"] =one_review
#         return context
    
# using detailed view for single review

class ReviewSingleView(DetailView):
    template_name="rev/one.html"
    model=Review

    
    