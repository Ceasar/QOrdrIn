# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from HackNY2011.app.models import Order, Options
from HackNY2011.app.signupform import OrderForm, OptionForm

from models import UserProfile

from signupform import SignUpForm

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
      return HttpResponse("Your account was successfully created! Feel free to start using the app!")
  else:
    form = SignUpForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('index.html', context)

def login(request):
  return render_to_response('login.html')

def menu(request):
  return render_to_response('menu.html')

@login_required
def order(request):
  if request.method == 'POST':
    form = OrderForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      order = Order(addr = data['addr'],
          city = data['city'],
          state = data['state'],
          zip = data['zip'],
          )
      order.save()
      return render_to_response('options.html')
  else:
    form = OrderForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('order.html', context)

@login_required
def options(request):
  if request.method == 'POST':
    form = OptionForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      options = Options(tip = data['tip'],
          delivery_addr = data['delivery_addr'],
          delivery_time = data['delivery_time'],
          )
      options.save()
      return HttpResponse("Your order was successfully placed!")
  else:
    form = OptionForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('options.html', context)
