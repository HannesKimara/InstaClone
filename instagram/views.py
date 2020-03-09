from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AbstractUser

from .forms import ImageForm
from .models import Profile, User, Image

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    all_images = Image.get_user_images(current_user)
    return render(request, 'index.html', {'images': all_images})

@login_required(login_url='/accounts/login/')
def myprofile(request):
    current_user = request.user

    all_images = Image.get_user_images(current_user)
    profile = Profile.objects.filter(user=current_user).first()

    return render(request, 'profile.html', {'user': current_user, 'images': all_images, 'profile' : profile})

@login_required(login_url='/accounts/login')
def create_post(request):
    current_user = request.user
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        print("I got the form")
        if form.is_valid():
            print("Form was valid")
            image = form.save(commit=False)
            image.user = current_user
            image.save()

            return render(request, 'index.html')
    else:
        form = ImageForm()

    return render(request, 'new_photo.html', {'form': form})
        

    
