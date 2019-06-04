from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Identification_Number = models.PositiveIntegerField(null=False)
    Age = models.PositiveIntegerField(null=False)
    Phone_Number = models.CharField(max_length=13, null=True, default=True)
    Driving = models.PositiveIntegerField(null=False)
    image = models.ImageField(upload_to='profile/', max_length=255, null=True,blank=True)

    def __str__(self):
        return self.user.username


class feedback(models.Model):

    username = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False,default='Feedback')
    message = models.CharField(max_length=1000, null=False)
    read = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

class booking(models.Model):
    fullname = models.CharField(max_length=100)
    car_price = models.PositiveIntegerField()
    car_make1 = models.CharField(max_length=1000)
    car_model1 = models.CharField(max_length=1000)
    phonenumber = models.CharField(max_length=13, null=True, default=True)
    pickupdate = models.DateField()
    days = models.PositiveIntegerField()
    user = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.fullname

class make1(models.Model):
    car_make = models.CharField(max_length=1000, null=False)
    description = models.TextField(max_length=1000, null=False)
    make_image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.car_make

class model1(models.Model):
    car_model = models.CharField(max_length=100, null=False)
    car_make = models.ForeignKey(make1, on_delete=models.CASCADE)
    car_price = models.PositiveIntegerField()
    car_image = models.ImageField()
    car_capacity = models.PositiveIntegerField()
    model_year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.car_model

class car(models.Model):
    car_make = models.ForeignKey(make1, on_delete=models.CASCADE)
    car_model = models.ForeignKey(model1, on_delete=models.CASCADE)
    number_plate = models.CharField(max_length=100, null=False)
    assigned = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
