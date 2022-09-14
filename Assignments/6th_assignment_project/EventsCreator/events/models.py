from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(name="Username", max_length=100, null=True)


class Category(models.Model):
    category_name = models.CharField(
        name="Category's Name", max_length=100, null=False)
    description = models.CharField(
        name="Description", max_length=500, null=True)

    def __str__(self):
        return f"Category: {self.category_name}, Description: {self.description}"


class Venue(models.Model):
    name = models.CharField(name="Venue's Name", max_length=100, null=False)
    location = models.CharField(name="Location", max_length=50, null=False)

    def __str__(self):
        return f"Venue / Address name: {self.name}, Location: {self.location}"


class Currency(models.Model):
    CURRENCY = (
        ("DOLLARS", "DOLLARS"),
        ("TAKA", "TAKA"),
        ("UAE DIRHAM", "UAE DIRHAM"),
        ("BITCOIN", "BITCOIN"),
        ("JAPANIAN YEN", "JAPANIAN YEN"),
    )
    name = models.CharField(name="Currency's name",
                            max_length=50, choices=CURRENCY)

    def __str__(self):
        return f"Currency's name: {self.name}"


class Time_Schedule(models.Model):
    timezone = timezone.now()
    start_date = models.DateField(max_length=50, name="Event Start Date")
    start_time = models.TimeField()


class Event(models.Model):
    EVENT_TYPE = (
        ("In-person", "In-person"),
        ("Streaming", "Streaming"),
        ("In-person and streaming", "In-person and streaming")
    )

    STREAM = (
        ("Secured Promotix", "Secured Promotix"),
        ("Unsecured - Other")
    )
    user = models.ForeignKey()
    title = models.TextField(name="Title", max_length=50, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=False, related_name="Category")
    event_type = models.CharField(
        name="Event Type", max_length=50, choices=EVENT_TYPE)
    stream = models.CharField(
        name="Stream Type", max_length=20, null=False, choices=STREAM)
    venue_or_address_name = models.CharField(
        name="Venue/Address name", max_length=100, null=False)
    time = models.ForeignKey(
        Time_Schedule, on_delete=models.SET_NULL, max_length=50, related_name="Time")
