import requests
from bs4 import BeautifulSoup

import json
import time

page = 1
url = "https://www.price.com.hk/category.php?c=100604&gp=56"
a = []

while page < 30:
    # Send a request to the website
    response = requests.get(f"{url}&page={page}")

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    products = soup.find_all('div', class_="item club-list-row")

    # Find all product details with class "product-detail-name"
    for product in products:
        d = {}
        product_names = product.find('div', class_='line line-01')
        d["names"] = product_names.text.strip()

        rating = product.find('span', class_="product-rating").find('img')['alt']
        if rating == "未有任何評分":
            d['rating'] = ""
        else:
            d['rating'] = rating
        

        # sell = product.find('div', class_="button product-detail-button")
        # if sell.text.strip() == "已售出":
        #     continue

        #water or hon
        prices = product.find_all('div', class_= 'listing-price-range')
        for price in prices:
            price_range = price.find_all('span', class_='text-price-number')
            if len(price_range) == 1:
                min_value = price_range[0].text
                max_value = price_range[0].text
            else:
                min_value = price_range[0].text
                max_value = price_range[1].text
            img = price.find('img')
            title = img['title']
            if title == "水貨":
                d["water_price_min"] = min_value
                d["water_price_max"] = max_value
            elif title == "行貨":
                d["hon_price_min"] = min_value
                d["hon_price_max"] = max_value

        #attributes
        attr_blk = product.find('div', class_="line line-04")
        attrs = attr_blk.find_all('div', class_="item-attr")
        for attr in attrs:
            label = attr.find('td', class_='attr-label')
            info = attr.find('td', class_='attr-info')
            if label is not None and info is not None:
                d[f"{label.text}"] = info.text



        # string = attr.text.strip().split("\n\n")
        # for i in range(len(string)):
        #     d[f"feature{i+1}"] = string[i]
        a.append(d)

    page = page + 1

data_str = json.dumps(a, indent=4, ensure_ascii=False)
with open("data/美容/美容儀器/纖體塑身儀.txt", "w", encoding="utf-8") as file:
    file.write(data_str)

