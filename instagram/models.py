from django.db import models
from django.contrib.auth.models import User as AbstractUser
from cloudinary.models import CloudinaryField

class DatabaseMethods:
    pass

class Profile(models.Model):
    profile_photo = CloudinaryField('profile_photo', default = "instagram/static/images/person_placeholder.jpg")
    bio = models.TextField(default = '')

class User(AbstractUser, models.Model):
    full_name = models.CharField(max_length=64)
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)

    def save_user(self):
        self.profile = Profile()
        self.profile.save()
        self.split_name = self.full_name.split()
        self.first_name, self.last_name = self.split_name[0], self.split_name[-1]

        self.save()

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=32)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.IntegerField(default=1)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)

class Followers(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="users")
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name="followers")

class ImageLike(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
