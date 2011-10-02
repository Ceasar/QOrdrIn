# Restaurant API

import api, re

def deliveryList(dT, addr):
  addr.validate()
  
  api._request("GET", "dl", dT._convertForRAPI(), addr.zip, addr.city, addr.street)
def deliveryCheck(rID, dT, addr):
  if not re.match(api._checkNums, rID):
    api._errs.append("r.deliveryCheck - validation - restaurant ID (invalid, must be numerical)")
  addr.validate()
  
  api._request("GET", "dc", rID, dT._convertForRAPI(), addr.zip, addr.city, addr.street)
def deliveryFee(rID, subtotal, tip, dT, addr):
  if not re.match(api._checkNums, rID):
    api._errs.append("r.deliveryCheck - validation - restaurant ID (invalid, must be numerical)")
  addr.validate()
  
  api._request("GET", "fee", rID, subtotal._convertForRAPI(), tip._convertForRAPI(), dT._convertForRAPI(), addr.zip, addr.city, addr.street)
def details(rID):
  if not re.match(api._checkNums, rID):
    api._errs.append("r.deliveryCheck - validation - restaurant ID (invalid, must be numerical)")
  return api._request("GET", "rd", rID)
