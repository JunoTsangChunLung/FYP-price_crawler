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

## Test if the code work

under test folder there will be 2 files: car_product_data.txt and test.py.

to test if the code is working, delete the car_product_data.txt file and run the test.py file to see if there is a new car_product_data.txt is created with data showing inside.

If everything is okay, now is time for you to do the web scarping.
