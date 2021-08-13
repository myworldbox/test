import json
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

with open('cookietest.json', 'r', newline='') as inputdata:
    cookies = json.load(inputdata)
curcookie = cookies[0]
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
driver.add_cookie(curcookie)
time.sleep(5)