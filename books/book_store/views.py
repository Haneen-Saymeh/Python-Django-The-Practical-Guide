from django.shortcuts import render
from .models import *
from django.db.models import Avg
from .forms import BookForm
from django import forms


def showAll(request):
    context={
        "books": Book.objects.all().order_by("rating"),
        "total_books":Book.objects.all().count(),
        "avg_rating": Book.objects.all().aggregate(Avg("rating"))

    }
 
    return render(request, "book_store/allbooks.html", context)

def onebook(request, slug):
    context={
        "book": Book.objects.get(slug=slug)

    }
    return render(request, "book_store/onebook.html", context) 

def fillForm(request):
    form=BookForm(request.POST)
    
    return render(request, "book_store/bookform.html", {'form':form})
