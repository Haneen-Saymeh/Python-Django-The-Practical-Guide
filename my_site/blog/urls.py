from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.starting_page, name="starting" ),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.one_post, name="one-post")
]