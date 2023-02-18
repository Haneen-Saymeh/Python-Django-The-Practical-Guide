
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showAll),
    path('<slug:slug>', views.onebook, name="one_book"),
    path('book', views.fillForm),
   
]