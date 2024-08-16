from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    phone_number = models.CharField(max_length=10)
    bio = models.TextField()
    address = models.TextField(max_length = 500)
    neighborhood = models.TextField(max_length = 500)

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField(max_length=50)
    condition = models.CharField(max_length=50, choices=[('New', 'New'), ('Used', 'Used')])
    image = models.ImageField(upload_to='product_images/')
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)