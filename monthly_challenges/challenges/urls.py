from django.urls import path
from django.views import View
from . import views
urlpatterns = [
    path("", views.allMonths),
    path('dash', views.mainpage),
    path('<month>',views.index),
    path('febu',views.feb),
    path('<int:month>', views.monthNumber),
    path('<str:month>', views.month, name="haneen"),
    
    
    
]
    