from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  phone = models.CharField(max_length=10)
  card_bill_addr = models.CharField(max_length=100)
  card_bill_city = models.CharField(max_length=100)
  card_bill_state = models.CharField(max_length=2)
  card_bill_zip = models.CharField(max_length=5)

class CreditCard(models.Model):
  user = models.OneToOneField(User)
  #THIS IS SKETCHY
  #full name of customer as appears on card
  card_name = models.CharField(max_length=30)
  card_number = models.CharField(max_length=16)
  card_cvc = models.CharField(max_length=4)  #card security code
  card_expiry = models.CharField(max_length=6)

class Order(models.Model):
  addr = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zip = models.CharField(max_length=5)
  tip = models.DecimalField(decimal_places=2, max_digits=5)
