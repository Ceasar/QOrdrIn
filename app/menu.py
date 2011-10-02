import json
import Ordrin

#def menu(restaurant_id):
Ordrin.api.initialize("BgmLvm7s4BGDCvuKu8bTaA", "https://r-test.ordr.in")

result = Ordrin.r.details("142") # TODO: replace value with restaurant_id

menu_items = []
for category in result['menu']:
    x = category['name']
    print "Category: " + x
    for item in category['children']:
        menu_items.append({'id': item['id'], 'name': item['name'], 'price': item['price']})

return render_to_response("menu.html", {'menu_items': menu_items})
        

