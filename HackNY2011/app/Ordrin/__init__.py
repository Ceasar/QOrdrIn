"""
Ordr.in Python Library Alpha
http://www.ordr.in

Copyright 2011
Last updated: July 11
"""

import datetime, re, r, u, o, api

class Address():
  def __init__(self, street, city, zip, street2="", state="", phone="", nick=""):
    self.nick = nick
    self.street = "+".join(street.split(" "))
    self.street2 = "+".join(street2.split(" "))
    self.city = "+".join(city.split(" "))
    self.zip = zip
    self.state = state
    self.phone = phone
  def validate(self, element="all"):
    if element == "zip" and not re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip):
      api._errs.append("Address object - validation - zip code (invalid)")
    elif element == "phone" and self.phone and not re.match("(^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$)", self.phone):
      api._errs.append("Address object - validation - phone number (invalid)")
    elif element == "city" and not re.match("[A-Za-z.-]", self.city):
      api._errs.append("Address object - validation - city (invalid, only letters/spaces allowed)")
    elif element == "state" and self.state and not re.match("^([A-Za-z]){2}$", self.state):
      api._errs.append("Address object - validation - state (invalid, only letters allowed and must be passed as two-letter abbreviation)")
    else:
      if not re.match("(^\d{5}$)|(^\d{5}-\d{4}$)", self.zip):
        api._errs.append("Address object - validation - zip code (invalid)")
      if self.phone and not re.match("^\(?(\d{3})\)?[- .]?(\d{3})[- .]?(\d{4})$", self.phone):
        api._errs.append("Address object - validation - phone number (invalid)")
      if not re.match("[A-Za-z.-]", self.city):
        api._errs.append("Address object - validation - city (invalid, only letters/spaces allowed)")
      if self.state and not re.match("^([A-Za-z]){2}$", self.state):
        api._errs.append("Address object - validation - state (invalid, only letters allowed and must be passed as two-letter abbreviation)")
  def _convertForRAPI(self):
    return self.zip + "/" + self.city + "/" + self.street;

class dTime(datetime.datetime):
  def asap(self):
    self.asap = 1
  def _strAPI(self, element):
    if element == "month":
      if self.month < 10:
        return "0" + str(self.month)
      else:
        return str(self.month)
    if element == "day":
      if self.day < 10: 
        return "0" + str(self.day)
      else:
        return str(self.day)
    if element == "hour":
      if self.hour < 10:
        return "0" + str(self.hour)
      else:
        return str(self.hour)
    if element == "minute":
      if self.minute < 10:
        return "0" + str(self.minute)
      else:
        return str(self.minute)
  def _convertForRAPI(self):
    if self.asap == 1:
      return "ASAP"
    else:
      return str(self.month) + "-" + str(self.day) + "+" + str(self.hour) + ":" + str(self.minute)

class Money():
  def __init__(self, amount):
    if not int(amount):
      api._errs.append(("validation", "money must be numerical"))
    else:
      self.amount = amount
  def _convertForRAPI(self):
    return str(self.amount)
