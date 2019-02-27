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
