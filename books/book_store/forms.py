from django.forms import ModelForm
from .models import *
from django import forms

class BookForm(ModelForm):
    # title= forms.CharField(max_length=50)
    # rating= forms.IntegerField()
    # author= forms.CharField(max_length=100)
    # is_bestSelling= forms.BooleanField()
    # slug= forms.SlugField(required=False)
    class Meta:
        model=Book
        # fields="__all__"
        fields=["title", "rating","author","is_bestSelling"]
        exclude = ['slug']