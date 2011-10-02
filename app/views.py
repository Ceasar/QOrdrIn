# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import UserProfile

from signupform import SignUpForm

def index(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      #user = User(username=username, password=password)
      return HttpResponse("Thanks!")
  else:
    form = SignUpForm()
  context = RequestContext(request, {'form': form})
  return render_to_response('index.html', context)

def login(request):
  return render_to_response('login.html')

def menu(request):
  return render_to_response('menu.html')

def options(request):
  return render_to_response('options.html')

def order(request):
  return render_to_response('order.html')
