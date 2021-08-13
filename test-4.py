#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Replace below path with the absolute path
# to chromedriver in your computer

options = webdriver.ChromeOptions();
options.add_argument("user-data-dir=~/.test")
# Create the folder. Change path accordingly

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
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