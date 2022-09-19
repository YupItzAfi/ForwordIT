from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User as Users

# Create your models here.


class User(models.Model):

    def __str__(self):
        return ""


class Categorie(models.Model):
    category_name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.category_name


class Venue(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Currencie(models.Model):
    CURRENCY = (
        ("DOLLARS", "DOLLARS"),
        ("TAKA", "TAKA"),
        ("UAE DIRHAM", "UAE DIRHAM"),
        ("BITCOIN", "BITCOIN"),
        ("JAPANIAN YEN", "JAPANIAN YEN"),
    )
    name = models.CharField(max_length=50, choices=CURRENCY)

    def __str__(self):
        return self.name


class Time_Schedule(models.Model):
    timezone = timezone.now()
    start_date = models.DateField(max_length=50)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return f"{self.start_date}, {self.start_time}-{self.end_time}"


class Event(models.Model):
    EVENT_TYPE = (
        ("In-person", "In-person"),
        ("Streaming", "Streaming"),
        ("In-person and streaming", "In-person and streaming")
    )

    STREAM = (
        ("Secured Promotix", "Secured Promotix"),
        ("Unsecured - Other", "Unsecured - Other"),
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="user")
    title = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(
        Categorie, on_delete=models.deletion.CASCADE, null=False, related_name="Category")
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    stream = models.CharField(max_length=20, null=False, choices=STREAM)
    venue_or_address_name = models.CharField(max_length=100, null=False)
    time = models.ForeignKey(
        Time_Schedule, on_delete=models.CASCADE, max_length=50, related_name="Time")
    person_ticket_name = models.CharField(max_length=50, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(
        max_digits=1000000, null=True, decimal_places=2)

    def __str__(self):
        return self.title


class Create_Ticket_Type(models.Model):
    TYPE = (
        ("GA Ticket", "GA Ticket"),
        ("VIP Ticket", "VIP Ticket"),
        ("Reserved Seating", "Reserved Seating"),
        ("Members-only Ticket", "Members-only Ticket"),
        ("Giveaway Ticket", "Giveaway Ticket"),
        ("Group Package Ticket", "Group Package Ticket"),
    )

    ticket_name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    created_date = models.DateField(
        max_length=50, auto_now=True, auto_created=True)

    def __str__(self):
        return self.ticket_name


class Ticket_Booking(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=False, related_name="user_id")
    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="event_id")
    ticket_id = models.ForeignKey(
        Create_Ticket_Type, null=True, on_delete=models.CASCADE, related_name="ticket_id")
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.PositiveSmallIntegerField(null=True)
    image = models.ImageField(
        upload_to="static/thumbnail/", max_length=300, blank=True)
    UID = models.PositiveIntegerField(null=True, auto_created=True)
    is_attend = models.BooleanField(null=True)
    is_active = models.BooleanField(null=True)
    creation_date = models.DateTimeField(
        auto_created=True, auto_now=True, null=False)

    def __str__(self):
        return self.name


class Payment(models.Model):
    pass

    def __str__(self):
        return super().__str__()


class Refund(models.Model):
    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="event_id_refund")
    reason = models.TextField(max_length=1000, null=True)
    demand_date = models.DateField(max_length=200)
    refund_date = models.DateField(
        auto_created=True, auto_now=True, null=False)

    def __str__(self):
        return self.demand_date


class Volunteer_Ticket(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=True, related_name="user_id_volunteer_ticket")
    name = models.CharField(max_length=100, null=True, unique=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone = models.PositiveIntegerField(null=True, unique=True)
    image = models.ImageField(
        upload_to="static/thumbnail/", max_length=300, blank=True, unique=True)
    UID = models.PositiveIntegerField(
        null=True, auto_created=True, unique=True)
    is_attend = models.BooleanField(null=True, unique=True)
    is_active = models.BooleanField(null=True, unique=True)
    creation_date = models.DateTimeField(
        auto_created=True, auto_now=True, null=False, unique=True)

    def __str__(self):
        return self.name
