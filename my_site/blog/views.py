from django.shortcuts import render

def starting_page(request):
    return render(request, "blog/start.html")

def posts(request):
    return render(request, "blog/posts.html")

def one_post(request, slug):
    return render(request, "blog/onepost.html")
