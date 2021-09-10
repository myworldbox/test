#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions();

#options.add_argument("user-data-dir=~/.test")

options.add_argument("user-data-dir=/Users/myworldbox/Library/Application Support/Google/Chrome")
options.add_argument('--disable-gpu')  # 禁用gpu
options.add_argument("--start-maximized")  # 視窗最大
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors') #忽略一些莫名的問題
# options.add_argument('--proxy-server={0}'.format(proxy.proxy))  # 加代理
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 開啟開發者模式
options.add_argument('--disable-blink-features=AutomationControlled')  # 谷歌88版以上防止被檢測
options.add_argument("--disable-blink-features")
#options.add_argument("--incognito");

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend Name' with the name of your friend or the name of a group
target = '"Friend Name"'

# Replace the below string with your own message
# I'm unsure why it needs two empty spaces in front of it.

string = " hi " + "Nachricht von Wichtel_Whatsapp"

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

print("Clicked")

default_input = "Schreib eine Nachricht"
# Change the Text with the default of the input-field

inp_xpath = "//div[contains(.,'" + default_input + "')]"
input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))).find_element_by_xpath('..')
input_box.send_keys(string)
# If the Text is written in the input field, use this line:
# input_box.send_keys(string + Keys.ENTER)