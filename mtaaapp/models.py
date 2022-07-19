from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



# Create your models here.
class Image(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
  image=CloudinaryField('image')
  image_desc=models.TextField()
  profile=models.ForeignKey(User, on_delete=models.CASCADE
  )

class Profile(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  prof_pic=CloudinaryField('image')
  bio=models.TextField()

class Comments(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  comment=models.CharField(max_length=400)