from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User)

  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  addr = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zip = models.CharField(max_length=5)
  phone = models.CharField(max_length=10)
  em = models.EmailField() #email

  #THIS IS SKETCHY
  #full name of customer as appears on card
  card_name = models.CharField(max_length=30)
  card_number = models.CharField(max_length=16)
  #card security code
  card_cvc = models.CharField(max_length=4)
  card_expiry = models.CharField(max_length=6)
  card_bill_addr = models.CharField(max_length=100)
  card_bill_addr2 = models.CharField(max_length=100, null=True)
  card_bill_city = models.CharField(max_length=100)
  card_bill_state = models.CharField(max_length=2)
  card_bill_zip = models.CharField(max_length=5)
