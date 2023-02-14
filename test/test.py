import requests
from bs4 import BeautifulSoup

import json

# Send a request to the website
response = requests.get("https://car.price.com.hk/?utm_source=price&utm_medium=menu&utm_campaign=car")

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('div', class_="wrapper product-detail")

a = []

# Find all product details with class "product-detail-name"
for product in products:
    d = {}
    product_names = product.find('div', class_='product-detail-name')
    prices = product.find('div', class_= 'product-detail-price').find_all('span', class_="text-price-number")
    attr = product.find('div', class_="product-detail-attr")
    d["names"] = product_names.text.strip()
    d["price"] = prices[0].text
    if 1 < len(prices):
        d["mprice"] = prices[1].text
    else:
        d["mprice"] = ""
    string = attr.text.strip().split("\n\n")
    for i in range(len(string)):
        d[f"attr{i+1}"] = string[i]
    a.append(d)

data_str = json.dumps(a, indent=4, ensure_ascii=False)
with open("car_product_data.txt", "w", encoding="utf-8") as file:
    file.write(data_str)