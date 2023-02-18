from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# this method is instead of using all other methods we don't even need the forms, we only need the models
class CreateProfileView(CreateView):
    template_name="profiles/create_profile.html"
    model= UserProfile
    fields="__all__"
    success_url="/profiles"

class ProfilesViews(ListView):
    model=UserProfile
    template_name="profiles/user_profile.html"
    context_object_name="profiles"




# Create your views here.
def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

# same process work for both images and files but changing the field type in models and forms, hence it will validate if it's not images it will not accept it
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form":form})

    def post(self, request):
        submitted_form=ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile= UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        else:
            return render(request, "profiles/create_profile.html", {"form":submitted_form})