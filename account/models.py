from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accountName = models.CharField(max_length=100)


class Profile(models.Model):
    profileId = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Place(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Container(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)


class InventoryItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    itemId = models.UUIDField(primary_key=True)
    container = models.ForeignKey(Container, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.IntegerField() #10
    current_value = models.IntegerField() #10
    # Interval of days by which the value will increase
    interval_of_days = models.IntegerField() #1
    # Ratio of increasing value after the interval
    increasing_ratio_in_percentage = models.IntegerField() #1
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    updated_at = models.DateField(auto_now=False, auto_now_add=True)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # interestPerTimeUnit = models.IntegerField()
    # timeUnit = models.DurationField()
    # compounded = models.BooleanField()
    # insuranceCoverage

    lentTo = models.CharField(max_length=100, blank=True, null=True)
    lentToFriend = models.BooleanField(default=False, blank=True, null=True)

    extraDetails = models.CharField(max_length=200, blank=True)
