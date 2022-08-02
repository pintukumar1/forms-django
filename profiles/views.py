from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import ProfileForm
from .models import UserProfile
# Create your views here.

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
                        
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            # store_file(request.files["image"])
            saveImage = UserProfile(image = request.FILES["user_image"])
            saveImage.save()
            return HttpResponseRedirect("/profiles")

        # image = request.FILES["image"]
        # print(image)
        # store_file(image)
        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })