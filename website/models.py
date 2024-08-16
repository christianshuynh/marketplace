from django.db import models

# Create your models here.
class Users(models.Model):
    userID = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField()
    location = models.charField(max_length=50)
    phone_number = models.charField(max_length=10)
    date_joined = models.DateTimeField()
    
class Profile(models.Model):
    
    
    