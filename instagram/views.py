from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as AbstractUser
from .models import Profile, User, Image

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def myprofile(request):
    current_user = request.user

    if User.objects.filter(user_ptr = current_user).first() != None:
        user_profile = User.objects.filter(user_ptr = current_user).first().profile
        new_user = current_user
    else:
        user_profile = Profile()
        user_profile.save()
        new_user = User(profile = user_profile)

        try:
            new_user.save()
        except Exception:
            pass

    all_images = Image.get_user_images(new_user)

    print(dir(current_user))
    return render(request, 'profile.html', {'in_user': new_user, 'user': current_user, 'images': all_images})

@login_required(login_url='/accounts/login')
def create_post(request):
    pass
        

    
