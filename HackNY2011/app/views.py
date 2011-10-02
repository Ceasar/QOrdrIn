# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

from HackNY2011.app.models import Order, Options
from HackNY2011.app.signupform import OrderForm, OptionForm, SignUpForm, CreditCardForm

from models import UserProfile

from bitlyapi.bitly import Api
import Ordrin
import json
import urllib, urllib2
import pickle


def thanks(request):
  return render_to_response("thanks.html")

def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = User(username = data['username'],
          password = data['password'],
          first_name = data['first_name'],
          last_name = data['last_name'],
          email = data['email'],
          )
      user.save()
      profile = UserProfile(user = user,
          phone = data['phone'],
          card_bill_addr = data['card_bill_addr'],
          card_bill_city = data['card_bill_city'],
          card_bill_state = data['card_bill_state'],
          card_bill_zip = data['card_bill_zip']
          )
      profile.save()
      return redirect('/creditcard/')
  else:
    form = SignUpForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('index.html', context)

def creditcard(request):
  if request.method == 'POST':
    form = CreditCardForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = request.USER
      profile = UserProfile(user = user,
          phone = data['phone'],
          )
      profile.save()
      credit_card = CreditCard(user=user,
          card_name = data['card_name'],
          card_number = data['card_number'],
          card_cvc = data['card_cvc'],
          card_expiry = data['card_expiry'],
          )
      credit_card.save()
      return HttpResponse("Your account was successfully created! Feel free to start using the app!")
  else:
    form = CreditCardForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('creditcard.html', context)


def login(request):
  return render_to_response('login.html')

def menu(request):
  Ordrin.api.initialize("BgmLvm7s4BGDCvuKu8bTaA", "https://r-test.ordr.in")
  bitly = Api(login = "o_5c6f85d1rm", apikey = "R_58d5a8e468494904fc23a57f4d1d10e1")

  result = Ordrin.r.details("142") # TODO: replace value with restaurant_id
  menu_items = []
  try:
    urls = pickle.load(open("urls.p", "rb"))
    print "OPENING urls.p"
  except IOError:
    urls = {}
    
  for category in result['menu']:
    for item in category['children']:
      long_url = 'http://afternoon-cloud-1710.herokuapp.com/order/?' + urllib.urlencode({'id': item['id']})
      if long_url in urls:
        short_url = urls[long_url]
      else:
        short_url = bitly.shorten(long_url) + ".qrcode"
        urls[long_url] = short_url
      if "descrip" in item:
        description = item['descrip']
      else:
        description = ''
      menu_items.append({'name': item['name'], 'price': item['price'], 'description': description, 'short_url': short_url})

  pickle.dump(urls, open("urls.p", "wb"))
  return render_to_response("menu.html", {'menu_items': menu_items})


@login_required
def order(request):
  return render_to_response('order.html')
