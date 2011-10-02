# Demo app to illustrate Python API functionality

import Ordrin, sys

print "Ordrin Python API Demo"
print "Defaulting to time: ASAP"
print "Defaulting to College Station, TX address"
place = Ordrin.Address("1 Main St", "College Station", "77840", "", "TX", "7777777777", "home")
when = Ordrin.dTime.now()
when.asap()

cmd = sys.argv[1] # API commands determined by argument at command-line

# remainder of app self-explanatory

def commands():
  if cmd == "r":
    restaurant()
  elif cmd == "u":
    user()
  elif cmd == "o":
    order()
  else:
    print "No API specified; restaurant API demo launching by default"
    restaurant()
  
def restaurant():
  Ordrin.api.initialize("mlJhC8iX4BGWVtn", "https://r-test.ordr.in")
  setAcct()
  
  action = raw_input("Which action would you like to run? [a] Delivery list [b] Delivery check [c] Delivery fee [d] Restaurant details (enter nothing to exit) ")
  if action == 'a':
    Ordrin.r.deliveryList(when, place)
  elif action == 'b':
    rid = raw_input("Restaurant ID? ")
    Ordrin.r.deliveryCheck(rid, when, place)
  elif action == 'c':
    rid = raw_input("Restaurant ID? ")
    sT = raw_input("Subtotal? ")
    tip = raw_input("Tip? ")
    Ordrin.r.deliveryFee(rid, sT, tip, when, place)
  elif action == 'd':
    rid = raw_input("Restaurant ID? ")
    Ordrin.r.details(rid)
  else:
    exit()
  commands()
  
def user():
  Ordrin.api.initialize("mlJhC8iX4BGWVtn", "http://u-test.ordr.in")
  
  action = raw_input("What kind of action would you like to run? [a] Account [b] Address [c] Card [d] Previous order[s] (enter nothing at any time to exit)")
  if action == 'a':
    subaction = raw_input("[a] Make account [b] Get account details [c] Update password")
    if subaction == 'a':
      email = raw_input("Email? ")
      password = raw_input("Password? ")
      fName = raw_input("First name? ")
      lName = raw_input("Last name? ")
      Ordrin.u.makeAcct(email, password, fName, lName)
    elif subaction == 'b':
      setAcct()
      Ordrin.u.getAcct()
    elif subaction == 'c':
      setAcct()
      newPass = raw_input("New password? ")
      Ordrin.u.updatePassword(newPass)
    else:
      exit()
  elif action == 'b':
    setAcct()
    subaction = raw_input("[a] Get address [b] Update address [c] Delete address ")
    if subaction == 'a':
      addrNick = raw_input("Address nickname? (enter none to return list) ")
      Ordrin.u.getAddress(addrNick)
    elif subaction == 'b':
      addrNick = raw_input("Address nickname? ")
      street = raw_input("Street? ")
      street2 = raw_input("Street addt'l? (optional) ")
      city = raw_input("City? ")
      state = raw_input("State? ")
      zip = raw_input("Zip? ")
      phone = raw_input("Phone? ")
      addr = Ordrin.Address(street, city, zip, street2, state, phone, addrNick)
      Ordrin.u.updateAddress(addr)
    elif subaction == 'c':
      addrNick = raw_input("Address nickname? ")
      Ordrin.u.deleteAddress(addrNick)
    else:
      exit()
  elif action == 'c':
    setAcct()
    subaction = raw_input("[a] Get card [b] Update card [c] Delete card ")
    if subaction == 'a':
      cardNick = raw_input("Card nickname? (enter none to return list) ")
      Ordrin.u.getCard(cardNick)
    elif subaction == 'b':
      cardNick = raw_input("Card nickname? ")
      name = raw_input("Name on card? ")
      number = raw_input("Card number? ")
      cvc = raw_input("Security card? ")
      expMo = raw_input("Expiry month? ")
      expYr = raw_input("Expiry year? ")
      street = raw_input("Street? ")
      street2 = raw_input("Street addt'l? (optional) ")
      city = raw_input("City? ")
      state = raw_input("State? ")
      zip = raw_input("Zip? ")
      phone = raw_input("Phone? ")
      addr = Ordrin.Address(street, city, zip, street2, state, phone)
      Ordrin.u.updateCard(cardNick, name, number, cvc, expMo, expYr, addr)
    elif subaction == 'c':
      cardNick = raw_input("Card nickname? ")
      Ordrin.u.deleteCard(cardNick)
    else:
      exit()
  elif action == 'd':
    setAcct()
    subaction = raw_input("Type in order ID (or nothing to list all): ")
    Ordrin.u.orderHistory(subaction)
  else:
    exit()
  commands()
  
def order():
  Ordrin.api.initialize("mlJhC8iX4BGWVtn", "https://o-test.ordr.in")
  setAcct()
  
  restID = raw_input("Restaurant ID? ")
  tray = raw_input("Tray? [itemid][quantity],[itemid2][quantity],... ")
  tip = raw_input("Tip? ")
  email = raw_input("Email? ")
  fName = raw_input("First name? ")
  lName = raw_input("Last name? ")

  cardNum = raw_input("Card number? ")
  csc = raw_input("Card security code? ")
  exp = raw_input("Expiration month + year? (MM/YY) ")
  Ordrin.o.submit(restID, tray, Ordrin.Money(int(tip)), when, email, fName, lName, place, fName + " " + lName, cardNum, csc, exp, place)
  
def setAcct():
  setUser = raw_input("Username? ")
  setPass = raw_input("Password? ")
  Ordrin.api.setCurrAcct(setUser, setPass)
  
commands()
