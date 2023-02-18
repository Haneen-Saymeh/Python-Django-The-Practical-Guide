from django.urls import path

from . import views

urlpatterns = [
    path("", views.review),
    path("thx", views.thank_you)
   
] 