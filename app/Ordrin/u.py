import api, hashlib

def makeAcct(email, password, firstName, lastName):
  # password before submission must be SHA256-encoded; to be fixed with API update
  # api._request("POST", "u", email, "password=" + hashlib.sha256(password).hexdigest(), "first_name=" + firstName, "last_name=" + lastName)
  api._request("POST", "uN", email, "password=" + password, "first_name=" + firstName, "last_name=" + lastName)
def getAcct(): # get details on current user
  api._request("GET", "u", api._currEmail)
def getAddress(addrNick=""):
  if addrNick:
    api._request("GET", "u", api._currEmail, "addrs", addrNick)
  else:
    api._request("GET", "u", api._currEmail, "addrs")
def updateAddress(addr): # Address must be passed using API's built-in Address object
  addr.validate()
  api._request("PUT", "u", api._currEmail, "addrs", addr.nick, "addr=" + addr.street, "addr2=" + addr.street2, "city=" + addr.city, "state=" + addr.state, "zip=" + addr.zip, "phone=" + addr.phone)
def deleteAddress(addrNick):
  api._request("DELETE", "u", api._currEmail, "addrs", addrNick)
def getCard(cardNick=""):
  if cardNick:
    api._request("GET", "u", api._currEmail, "ccs", cardNick)
  else:
    api._request("GET", "u", api._currEmail, "ccs")
def updateCard(cardNick, name, number, cvc, expiryMonth, expiryYear, addr):
  addr.validate()
  api._request("PUT", "u", api._currEmail, "ccs", cardNick, "name=" + name, "number=" + number, "cvc=" + cvc, "expiry_month=" + expiryMonth, "expiry_year=" + expiryYear, "bill_addr=" + addr.street, "bill_addr2=" + addr.street2, "bill_city=" + addr.city, "bill_state=" + addr.state, "bill_zip=" + addr.zip)
def deleteCard(cardNick):
  api._request("DELETE", "u", api._currEmail, "ccs", cardNick)
def orderHistory(orderID=""): # if orderID left blank, all previous orders returned: ID returns specific details of order
  if orderID:
    api._request("GET", "u", api._currEmail, "order", orderID)
  else:
    api._request("GET", "u", api._currEmail, "orders")
def updatePassword(password):
  api._request("PUT", "u", api._currEmail, "password", "password=" + hashlib.sha256(password).hexdigest())