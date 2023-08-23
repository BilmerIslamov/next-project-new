import requests


def get_next_api():
    r = requests.get("https://bilmervipapi.pythonanywhere.com/next_api/all-product/")
    data = r.json()
    return data


dataApi = get_next_api()

api = []

for i in dataApi:
    product_id = i["id"]
    api.append(product_id)

print(api)
