# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

from signupform import SignUpForm

def index(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      return HttpResponse("Thanks!")
  else:
    form = SignUpForm()
  context = {'form': form}
  return render_to_response('index.html', context)

def login(request):
  return render_to_response('login.html')

def create(request):
  return render_to_response('create.html')

def menu(request):
  
  return render_to_response('menu.html')

def order(request):
  return render_to_response('order.html')
