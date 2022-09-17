from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(name="Username", max_length=100, null=True)

    def __str__(self):
        return f"Username: {self.name}"


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
    name = models.CharField(max_length=50, choices=CURRENCY)

    def __str__(self):
        return f"Currency's name: {self.name}"


class Time_Schedule(models.Model):
    timezone = timezone.now()
    start_date = models.DateField(max_length=50)
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)

    def __str__(self):
        return f"Start Date: {self.start_date}.\nStart Time: {self.start_time}, End Time: {self.end_time}."


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
        User, on_delete=models.DO_NOTHING, null=False, related_name="user")
    title = models.TextField(name="Title", max_length=50, null=False)
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, null=False, related_name="Category")
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    stream = models.CharField(max_length=20, null=False, choices=STREAM)
    venue_or_address_name = models.CharField(max_length=100, null=False)
    time = models.ForeignKey(
        Time_Schedule, on_delete=models.DO_NOTHING, max_length=50, related_name="Time")
    person_ticket_name = models.CharField(max_length=50, null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.DecimalField(
        max_digits=100000, null=True, decimal_places=10)

    def __str__(self):
        return f"Title: {self.title}, User: {self.user}, Price: {self.price}, Time: {self.time}"


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
    type = models.CharField(max_length=50, null=False, choices=TYPE)
    created_date = models.DateField(
        max_length=50, auto_now=True, auto_created=True)

    def __str__(self):
        return f"Name: {self.ticket_name}, Type: {self.type}, Creation Date: {self.created_date}"


class Ticket_Booking(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=False, related_name="user_id")
    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="event_id")
    ticket_id = models.ForeignKey(
        Create_Ticket_Type, null=False, on_delete=models.CASCADE, related_name="ticket_id")
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=100, null=True)
    phone = models.PositiveSmallIntegerField(null=False)
    image = models.ImageField(
        upload_to="static/thumbnail/", max_length=300, blank=True)
    UID = models.PositiveIntegerField(null=False, auto_created=True)
    is_attend = models.BooleanField(null=True)
    is_active = models.BooleanField(null=True)
    creation_date = models.DateTimeField(
        auto_created=True, auto_now=True, null=False)

    def __str__(self):
        return f"Name: {self.name}, \
                UID: {self.UID}, \
                Is attending: {self.is_attend}, \
                Is active: {self.is_active}, \
                Creation date: {self.creation_date}"


class Payments(models.Model):
    pass


class Refund(models.Model):
    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="event_id_1")
    reason = models.TextField(max_length=1000, null=True)
    demand_date = models.DateField(max_length=200)
    refund_date = models.DateField(
        auto_created=True, auto_now=True, null=False)


class Volunteer_Ticket(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, null=False, related_name="user_id_1")
    name = models.CharField(max_length=100, null=False, unique=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone = models.PositiveIntegerField(null=True, unique=True)
    image = models.ImageField(
        upload_to="static/thumbnail/", max_length=300, blank=True, unique=True)
    UID = models.PositiveIntegerField(
        null=False, auto_created=True, unique=True)
    is_attend = models.BooleanField(null=True, unique=True)
    is_active = models.BooleanField(null=True, unique=True)
    creation_date = models.DateTimeField(
        auto_created=True, auto_now=True, null=False, unique=True)

    def __str__(self):
        return f"Name: {self.name}, \
                UID: {self.UID}, \
                Is attending: {self.is_attend}, \
                Is active: {self.is_active}, \
                Creation date: {self.creation_date}"
