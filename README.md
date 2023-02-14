# FYP-price_crawler
This repository stores the code to crawl the information from [price](https://www.price.com.hk/) for educational purpose

## Description:

There are three folders in total:<hr>

The test folder is for testing if the code is working.

The code folder is to run the code to scape the information from price for specific product type.

The data folder is the folder storing the data crawled from the running of python code from code folder.

## Installation:

You will need to download [Python](https://www.python.org/downloads/).
It is safer for you to not install the lastest version, better using Python 3.9 or 3.10

You can also use some extension tools such as conda and anaconda.

<hr>

It is better for you to create a virtual environment for this project.

```bash
pip install virtualenv

python<version> -m venv <virtual-environment-name>
```

It is okay if you don't want to create one becasue we are not using too many librares here.

<hr>

After you have download python, it is time for you to download the librares:

Here we are using 4 librares:

```python
import requests
from bs4 import BeautifulSoup

import json
import time
```

But you only need to install two of them which are requests and BeautifulSoup

Run the command in your terminal to install them:

```bash
pip3 install requests
```

```bash
pip3 install BeautifulSoup
```

## Test if the code work:

under test folder there will be 2 files: car_product_data.txt and test.py.

to test if the code is working, delete the car_product_data.txt file and run the test.py file to see if there is a new car_product_data.txt is created with data showing inside.

If everything is okay, now is time for you to do the web scarping.

## How the code works:

If price.com have not change any class element, the code should be working fine:

The folder inside code is classified by the category in price.com.hk, inside them there is the crawler for each subcategory:

For example: for 通訊/手提電話, there are tablet, smartphone...

In smartphone.py, the website in the code refers to the page scaping the smartphone's product data

```python
response = requests.get(f"https://www.price.com.hk/category.php?c=100005&gp=10&page={page}")
```

Above this line of code, for line 10, you can see there is a while loop for page less than a specific number

```python
while page < 20:
```

The page number is the total number of page you want to srape, in this case, the crawler will scape the product data from page 1 to page 19.

Then at the end of the code:

```python
with open("data/通訊/手提電話/smart_phone.txt", "w", encoding="utf-8") as file:
    file.write(data_str)
```

The path "data/通訊/手提電話/smart_phone.txt" is a relative path.

Therefore, <h3><b>make sure you run the code in the right place. </b></h3>

How to check if I am in the right place? <hr>

You should know where you put your code in.

For example, I have created a file in the desktop called dev, inside dev, I have created a file called FYP, inside it there's a file called dev, and inside dev there's a file called price_cawler, then is the code

For this, when I run my Python code from the terminal, it would be something like:

```bash
(base) junotsang@Junos-MacBook-Pro price_crawler % python code/通訊/手提電話/smart_phone.py
```

you can see the python file is located at Desktop/FYP/dev/price_cralwer/code/通訊/手提電話/
and the place I run my code is price_cralwer, therefore the relative path is price_crawler/data/通訊/手提電話/smart_phone.txt

you can check the path to see if there's any folder, it would probably throw error if you are not following this.
