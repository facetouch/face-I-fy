from django.db import models


# class Person():
#     pass


class Event(models.Model):
    event_name = models.CharField(default="default", max_length=10)
    time_stamp = models.CharField(default="", max_length=100)
    is_consumed = models.BooleanField(default=False)


# class Item():

#


# class Cart:
#     person_id = Models.

class Image(models.Model):
    url = models.CharField(default="", max_length=100)


class Items(models.Model):
    name = models.CharField(default="", max_length=50)
    description = models.CharField(default="", max_length=100)
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    url = models.OneToOneField(Image, on_delete=models.CASCADE)


class Sections(models.Model):
    name = models.CharField(default="", max_length=50)
    section = models.ForeignKey(Items)
