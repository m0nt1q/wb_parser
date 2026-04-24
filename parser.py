import requests

cookies = {}

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzcwNDI0ODUsInVzZXIiOiIxMjkxNjYxNzEiLCJzaGFyZF9rZXkiOiIzMSIsImNsaWVudF9pZCI6IndiIiwic2Vzc2lvbl9pZCI6ImY5ZGZlNmUzMDFiYTRiOTg5ODhhYWZmOGE2MTkyZjE4IiwicGhvbmUiOiJEejZPbmJ3MnUvYUF5algzaVJzM2dnPT0iLCJ2YWxpZGF0aW9uX2tleSI6IjQ0ZjZiM2Y3ZDc2OWVlNmQyMGIzNzI0YTlmMTg5NjcxZTczNzNlZjU0MzgzNTRlZTBmZDdhYzFkMTUwNGIwN2YiLCJ1c2VyX3JlZ2lzdHJhdGlvbl9kdCI6MTY5ODA3NTI1MywidmVyc2lvbiI6Mn0.V_I3UZxFI3piaXoxZGi-ZJQDZGCAta9FSpTjIvo0-7htgO2_GUuFDS2iMWEyOfSe3sX9Usv6mNLN37zPodfj8TlsB4IuZi4wAYh-PCv5o_cvYS7XB760ND7uu4Tt_INAyZ4O7Ktl33QDfS4mpKx8UYh7rZ7Ecg0s9WKC-hx3fFK5khStkOpyQ3AbuBjkhjE7aOU7OeJzHalCf8N7vZL5ItAiPAVrbW00TRFIvwfL7aNLJtKq-i441rBH9YXxlvtv9NKZr_vYGwkmRb2FsZXzVLNWkuC7IewPL94nBa8ubq7xQvsBBTNbnWT3W6RwzjGVTP_uKknnUuDNIn5kV8eqZA',
    'deviceid': 'site_ad16f58d25b24c918fbb49f7e14b46a1',
    'priority': 'u=1, i',
    'referer': 'https://www.wildberries.ru/catalog/210863467/detail.aspx?targetUrl=MI',
    'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
    'x-requested-with': 'XMLHttpRequest',
    'x-spa-version': '14.7.0',
   
}

params = {
    'appType': '1',
    'curr': 'rub',
    'dest': '-3349396',
    'spp': '30',
    'hide_vflags': '4294967296',
    'mdg': '106',
    'ab_testing': 'false',
    'lang': 'ru',
    'nm': '210863467',
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