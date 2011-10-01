# Create your views here.
from django.http import HttpResponse

def index(request):
  return HttpResponse("Index!")

def login(request):
  return HttpResponse("Login")

def create(request):
  return HttpResponse("Create")

def menu(request):
  return HttpResponse("Menu")

def order(request):
  return HttpResponse("Order")
