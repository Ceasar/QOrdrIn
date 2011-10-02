# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import UserProfile

from signupform import SignUpForm
from bitlyapi.bitly import Api
import Ordrin
import json
import urllib

def index(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = User(username = data['username'],
          password = data['password'],
          first_name = data['first_name'],
          last_name = data['last_name'],
          email = data['email']
          )
      user.save()
      profile = UserProfile(user = user,
          phone = data['phone'],
          card_name = data['card_name'],
          card_number = data['card_number'],
          card_cvc = data['card_cvc'],
          card_expiry = data['card_expiry'],
          card_bill_addr = data['card_bill_addr'],
          card_bill_city = data['card_bill_city'],
          card_bill_state = data['card_bill_state'],
          card_bill_zip = data['card_bill_zip']
          )
      profile.save()
      return HttpResponse("Thanks!")
  else:
    form = SignUpForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('index.html', context)

def login(request):
  return render_to_response('login.html')

def menu(request):
  Ordrin.api.initialize("BgmLvm7s4BGDCvuKu8bTaA", "https://r-test.ordr.in")
  bitly = Api(login = "o_5c6f85d1rm", apikey = "R_58d5a8e468494904fc23a57f4d1d10e1")
  result = Ordrin.r.details("142") # TODO: replace value with restaurant_id
  menu_items = []
  for category in result['menu']:
    x = category['name']
    for item in category['children']:
      short_url = bitly.shorten('http://afternoon-cloud-1710.herokuapp.com/order/?' + urllib.urlencode({'id': item['id']})) + ".qrcode"
      menu_items.append({'id': item['id'], 'name': item['name'], 'price': item['price'], 'url': short_url})

  return render_to_response("menu.html", {'menu_items': menu_items})


@login_required
def order(request):
  return render_to_response('order.html')

@login_required
def options(request):
  return render_to_response('options.html')
