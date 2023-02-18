from django import forms
from .models import *


# class ReviewForm(forms.Form):
#     user_name= forms.CharField(label="your name",max_length=10, error_messages={
#         "required":"your name must not be empty",
#         "max_length": "please enter a shorter name"
#     })

#     review_text=forms.CharField(label="your feedback", widget=forms.Textarea, max_length=200)
#     rating= forms.IntegerField(label="your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = "__all__"

        labels={
            "user_name":"your name",
            "review_text":"your feedback",
            "rating":"your rating"
        }