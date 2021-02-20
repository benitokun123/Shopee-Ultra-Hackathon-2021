import requests
import json

BASE = "https://api.hackathon2021.shopee.sg/"
API_KEY = "CSIvMfJ6dDFWPhTIL3sA"
USER_KEY = "b3RURE9LV0VmNEdKYkNNN6Od8sh7vmKjewOwBOr2Oz4FdR8pGs7bBdfCBhxMr6WiUtHXae41WPRBjLp94Err99d0bk1VzrRVcbG8yUIUuQ8iXaCufNRkC2QsLfxKHhrKNc8nYHZ8dmS+k8zwvs+pFAhjoOQ7qrP7ba4sAr6e7f23zF/lNSTl06STs0LgY62D9ySkOkZd82jvm4vjFAoYPSGyUg29ikhBIg/ft7kZ61hlQCReGxGMtRY3CkDDFWgX"

# non-authenticated 
item_get_info = "item/get_info"
item_search = "item/search"
shop_get_info = "shop/get_info"
shop_get_items = "shop/get_items"
shop_get_vouchers = "shop/get_vouchers"

# authenticated
user_generate_token = "user/generate_token" # not to be used outside browser
user_get_info = "user/get_info"
user_get_vouchers = "user/get_vouchers"
user_get_cart_items = "user/get_cart_items"

headers = {'X-Hackathon-Token': API_KEY}
# print(headers)
# response = requests.get(BASE + item_get_info, headers = headers, params = {"item_id" : 1, "shop_id" : 1})
# print(response)
# print(response.text)

def search_item(keyword: str):
    response = requests.get(BASE + item_search, headers = headers, params = {'keyword' : keyword, 'offset': 0, 'limit': 30})
    print(response)
    print(response.text)
    dic = json.loads(response.text)
    print(json.dumps(dic, indent = 4))
    data = dic['data']['items']

    for item in data:
        print(item['item_id'])
        print(item['shop_id'])
        print("")

def get_item_info(shop_id : int, item_id : int):
    response = requests.get(BASE + item_get_info, headers = headers, 
        params = {'shop_id' : shop_id, 'item_id': item_id})
    print(response)
    response_json = json.loads(response.text)
    print(json.dumps(response_json, indent = 4))

if __name__ == "__main__":
    keyword = input("Enter keyword for search: ")
    search_item(keyword)
    # get_item_info(170372281, 6232138548)