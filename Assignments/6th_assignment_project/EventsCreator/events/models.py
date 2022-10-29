from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User as Users
from django.core.validators import MinValueValidator

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
    name = models.CharField(max_length=100, null=False,
                            blank=True, unique=True)
    location = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Currencie(models.Model):
    CURRENCY = (
        ("usd", "Dollars"),
        ("bdt", "Taka"),
        ("aed", "UAE Dirham"),
        ("kwd", "Kuwait Dinar"),
        ("jpy", "Japanian Yen"),
    )
    name = models.CharField(max_length=50, null=False, choices=CURRENCY)

    def __str__(self):
        return [proper_locale[0] for (locale, proper_locale) in self.CURRENCY if self.name in locale]


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
        ("In-person and Streaming", "In-person and Streaming")
    )

    STREAM = (
        ("Secured_Promotix", "Secured Promotix"),
        ("Unsecured-Other", "Unsecured - Other"),
    )
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True, related_name="user")
    title = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(
        Categorie, on_delete=models.deletion.CASCADE, null=False, related_name="Category")
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    stream = models.CharField(max_length=20, null=False, choices=STREAM)
    venue_or_address_name = models.ForeignKey(
        Venue, on_delete=models.deletion.CASCADE, max_length=100, null=True, related_name="venue_or_address_name")
    time = models.ForeignKey(
        Time_Schedule, on_delete=models.CASCADE, max_length=50, related_name="Time")
    person_ticket_name = models.CharField(max_length=50, null=True)
    quantity = models.PositiveIntegerField(
        null=False, validators=[MinValueValidator(1)])
    price = models.DecimalField(
        max_digits=99999999, null=False, decimal_places=2)

    def __str__(self):
        return self.title


class Create_Ticket_Type(models.Model):
    TYPE = (
        ("ga_ticket", "GA Ticket"),
        ("vip_ticket", "VIP Ticket"),
        ("reserved_seating", "Reserved Seating"),
        ("members_only_ticket", "Members-only Ticket"),
        ("giveaway_ticket", "Giveaway Ticket"),
        ("group_package_ticket", "Group Package Ticket"),
    )

    ticket_name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=50, null=True, choices=TYPE)
    created_date = models.DateField(
        max_length=50, auto_now=True, auto_created=True)

    def __str__(self):
        return self.ticket_name


class Ticket_Booking(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.DO_NOTHING, null=False, related_name="ticket_user_id")
    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="ticket_event_id")
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
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return super().__str__()


class Refund(models.Model):
    class reasons(models.TextChoices):
        duplicate = '1', 'Duplicate'
        fradulent = '2', 'Fraudulent'
        requested_by_customer = '3', 'Requested by Customer'
        expired_uncaptured_charge = '4', 'Expired uncaptured charge'

    event_id = models.ForeignKey(
        Event, on_delete=models.PROTECT, related_name="event_id_refund")
    reason = models.CharField(
        max_length=25, null=True, choices=reasons.choices)
    demand_date = models.DateField(max_length=200)
    refund_date = models.DateField(
        auto_created=True, auto_now=True, null=False)

    def __str__(self):
        return self.demand_date


class Volunteer_Ticket(models.Model):
    user_id = models.ForeignKey(
        Users, on_delete=models.DO_NOTHING, null=True, related_name="user_id_volunteer_ticket")
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
