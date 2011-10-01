# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
  return render_to_response('index.html')

def login(request):
  return render_to_response('login.html')

def create(request):
  return render_to_response('create.html')

def menu(request):
  
  return render_to_response('menu.html')

def order(request):
  return render_to_response('order.html')
