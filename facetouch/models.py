from django.db import models
from datetime import datetime


# class Person():
#     pass


class Event(models.Model):
    event_name = models.CharField(default="default", max_length=10)
    time_stamp = models.CharField(default="", max_length=100)
    is_consumed = models.BooleanField(default=False)


class Image(models.Model):
    url = models.CharField(default="", max_length=100)


class Section(models.Model):
    name = models.CharField(default="", max_length=50)


class Item(models.Model):
    name = models.CharField(default="", max_length=50)
    description = models.CharField(default="", max_length=100)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    section = models.ForeignKey(Section)

class User(models.Model):
    userId = models.IntegerField(max_length=5000,primary_key=True)

class Cart(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)
