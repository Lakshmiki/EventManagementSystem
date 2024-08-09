from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
class HallModel(models.Model):
    name=models.CharField(max_length=50)
    capacity=models.IntegerField()
    is_available=models.BooleanField(default=True)
    def __str__(self):
        return self.name
class Venue_event(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')
class Event_one_model(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/')


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    rating = models.FloatField(default=0.0)

class Venue(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='venue_images/')


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    date = models.DateField()
    half = models.CharField(max_length=10, choices=[('first', 'First Half'), ('second', 'Second Half')])
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
class FoodPackage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_available = models.IntegerField()
    image=models.ImageField(upload_to='image/')



    def __str__(self):
        return self.name


class Vendor_model(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Consider using Django's hashing mechanism
    company_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class Hall_last_Model(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return self.name
class Booking_last_model(models.Model):
    hall = models.ForeignKey(Hall_last_Model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hall.name} - {self.date} by {self.user.username}"

















