from django.db import models
from django.contrib.auth.models import User as AbstractUser
from cloudinary.models import CloudinaryField

class ModelMethods:
    """
    Define CRUD operation methods for db models
    """
    def save_model(self):
        """
        Save relational model data to database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.save()

    def delete_model(self):
        """
        Delete relational model data from database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.delete()

    def update_model(self, **kwargs):
        """
        Update relational model data in database

        Args:
            kwargs: model attributes to be updated
        Returns:
            None (NoneType)
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.save()

class Profile(models.Model, ModelMethods):
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

    def deactivate_user(self):
        self.is_active = False
        self.save()

class Image(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=32)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.IntegerField(default=1)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()

class Comment(models.Model, ModelMethods):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)

class Followers(models.Model, ModelMethods):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="users")
    follower = models.ForeignKey(User, on_delete = models.CASCADE, related_name="followers")

class ImageLike(models.Model, ModelMethods):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
