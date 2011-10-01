from django import forms
from django.contrib.localflavor.us.forms import *

class SignUpForm(forms.Form):
  first_name = forms.CharField(max_length=30)
  last_name = forms.CharField(max_length=30)
  addr = forms.CharField(max_length=100)
  city = forms.CharField(max_length=100)
  state = USStateField()
  zip = USZipCodeField()
  phone = USPhoneNumberField()
  em = forms.EmailField() #email

  #THIS IS SKETCHY
  #full name of customer as appears on card
  card_name = forms.CharField(max_length=30)
  card_number = forms.CharField(max_length=16)
  #card security code
  card_cvc = forms.CharField(max_length=4)
  card_expiry = forms.CharField(max_length=6)
  card_bill_addr = forms.CharField(max_length=100)
  card_bill_addr2 = forms.CharField(max_length=100)
  card_bill_city = forms.CharField(max_length=100)
  card_bill_state = USStateField()
  card_bill_zip = USZipCodeField()
