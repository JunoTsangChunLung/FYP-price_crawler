import requests
from bs4 import BeautifulSoup

import json
import time

page = 1
a = []

while page < 5:
    # Send a request to the website
    response = requests.get(f"https://car.price.com.hk/product/list?ptype=1&q=model+s&page={page}")

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_="wrapper wrapper-product")

    # Find all product details with class "product-detail-name"
    for product in products:
        d = {}
        product_names = product.find('div', class_='product-name')
        sell = product.find('div', class_="button product-detail-button")
        if sell.text.strip() == "已售出":
            continue
        prices = product.find('div', class_= 'product-price').find_all('span', class_="text-price-number")
        attr = product.find('div', class_="product-attribute")
        d["names"] = product_names.text.strip()
        d["mprice"] = prices[0].text
        if 1 < len(prices):
            d["sprice"] = prices[1].text
        else:
            d["sprice"] = prices[0].text
        string = attr.text.strip().split("\n\n")
        for i in range(len(string)):
            d[f"feature{i+1}"] = string[i]
        a.append(d)

    page = page + 1
    time.sleep(1)

data_str = json.dumps(a, indent=4, ensure_ascii=False)
with open("data/汽車/私家車/tesla_model_S.txt", "w", encoding="utf-8") as file:
    file.write(data_str)

