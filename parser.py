import requests

cookies = {}

headers = {

}

params = {

}

response = requests.get(
    'https://www.wildberries.ru/__internal/card/cards/v4/detail',
    params=params,
    cookies=cookies,
    headers=headers,
)
data = response.json()

product_data = data['products'][0]

current_price = product_data['sizes'][0]['price']['product']/100
name = product_data['name']

print(f"Товар: {name}")
print(f"Текущая цена на товар: {current_price} руб.")
