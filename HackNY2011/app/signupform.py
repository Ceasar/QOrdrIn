from django import forms
from django.contrib.localflavor.us.forms import *

from models import *

class OrderForm(forms.Form):
  addr = forms.CharField(label='Address', max_length=100)
  city = forms.CharField(max_length=100)
  state = USStateField()
  zip = USZipCodeField(label='Zip Code')
  tip = forms.DecimalField(label='Tip', decimal_places=2)

class SignUpForm(forms.Form):
  username = forms.CharField(label='Username', max_length=30)
  password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
  password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput(render_value=False))

  first_name = forms.CharField(label='First Name', max_length=30)
  last_name = forms.CharField(label='Last Name', max_length=30)
  phone = USPhoneNumberField()
  email = forms.EmailField(label='Email')

  card_bill_addr = forms.CharField(label='Address', max_length=100)
  card_bill_city = forms.CharField(label='City', max_length=100)
  card_bill_state = USStateField(label='State')
  card_bill_zip = USZipCodeField(label='Zip Code')

class CreditCardForm(forms.Form):
  #THIS IS SKETCHY
  #full name of customer as appears on card
  card_name = forms.CharField(label='Name on card', max_length=30)
  card_number = forms.CharField(max_length=16)
  #card security code
  card_cvc = forms.CharField(label='Security Code', max_length=4)
  card_expiry = forms.CharField(label='Expiration Date', max_length=6)

class OptionForm(forms.Form):
    tip = forms.DecimalField(label='Tip', decimal_places=2)
    delivery_addr = forms.CharField(label='Delivery Address', max_length=100)
    delivery_time = forms.DateTimeField(label='Delivery Time')
