import requests
import json

BASE = "http://127.0.0.1:5000/"
# BASE = "https://flaskshopeebackend.herokuapp.com/"
# id = 1

# response = requests.put(BASE + "wishlist/20", {'item_id' : 12, 'shop_id': 123, 'post' : "apiewfjpweifje" })
# print(response.message)
response = requests.get(BASE + "/friends/1")
print(response)
print(response.json())