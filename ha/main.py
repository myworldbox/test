# Copyright© 2020. VL Some rights reserved.
# https://myworldbox.github.io/

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from random import randint

import urllib.request
import numpy
import pandas
import time
import ssl

key = "1d_QazTaI4Awe8fXhoYXRqWE8o02ivy9Vukifgphb5F0"
gid = "1428758060"
file = "WhatGod"

count = 0

ssl._create_default_https_context = ssl._create_unverified_context

from selenium import webdriver
import json
import time

from webdriver_manager.chrome import ChromeDriverManager

from csv import DictReader

print('send cookie')

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://facebook.com/")

with open('main.csv', encoding='utf-8-sig') as f:
    reader = DictReader(f)
    lists = list(reader)

for i in lists:
    driver.add_cookie(i)

driver.refresh()

time.sleep(15)