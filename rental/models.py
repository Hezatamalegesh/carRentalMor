from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Equipment(models.Model):
    equipment = models.CharField(max_length=50)
    pass

class Car(models.Model):
    ENGINE_TYPES = [
        ("benzynowy", "Benzynowy"),
        ("diesel", "Diesel"),
        ("hybrydowy", "Hybrydowy"),
        ("elektryczny", "Elektryczny"),
        ("wodorowy", "Wodorowy")
    ]
    GEARBOX_TYPES = [
        ("automatyczna", "Automatyczna"),
        ("manualna", "Manualna"),
        ("pol_automatyczna", "Polautomatyczna"),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=20, choices=ENGINE_TYPES)
    seats_count = models.PositiveBigIntegerField()
    doors_count = models.PositiveSmallIntegerField()
    fuel_usage = models.FloatField()
    engine_power = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=20)
    equipment = models.ManyToManyField(Equipment)
    gearbox_types = models.CharField(max_length=20, choices=GEARBOX_TYPES)
    available = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    pass



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    post_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    building_no = models.CharField(max_length=10)
    appartment_no = models.CharField(max_length=10, blank=True, default='', help_text='To pole jest opcjonalne.')
    pass

class User(User):
    IDENTITY_DOCUMENT_TYPES = [
        ("dowod", "Dowód osobisty"),
        ("passport", "Paszport"),
        ("prawo_jazdy", "Prawo jazdy"),
    ]
    phone = models.CharField(max_length=20)
    identity_document_no = models.CharField(max_length=20)
    identity_document_type = models.CharField(max_length=20, choices=IDENTITY_DOCUMENT_TYPES)
    pass


class Order(models.Model):
    PAYMENT_METHODS = [
        ("karta", "Karta"),
        ("gotowka", "Gotówka"),
        ("przelew", "Przelew"),
        ("blik", "Blik"),
    ]
    customer = models.ForeignKey(User, on_delete=models.RESTRICT)
    car = models.ForeignKey(Car, on_delete=models.RESTRICT)
    order_value = models.DecimalField(max_digits=10, decimal_places=2)
    declared_order_duration = models.DurationField()
    pickup_date = models.DateTimeField()
    return_date = models.DateTimeField()
    deposit = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    payment_status = models.BooleanField()
    pass

