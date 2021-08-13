from selenium import webdriver
import json
import time

from webdriver_manager.chrome import ChromeDriverManager
print('get cookie')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
time.sleep(15)
cookies = driver.get_cookies()
with open('cookietest.json', 'w', newline='', encoding='utf-8-sig') as outputdata:
    json.dump(cookies, outputdata)
