from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

print("Getting you chrome browser!!!!")
driver  = webdriver.Chrome()


driver.maximize_window()
#driver.implicitly_wait(3)
#time.sleep(3)
driver.get("https://www.google.com/")
#search_box = driver.find_element("name","q")
#search_box = driver.find_element("id","APjFqb")
#search_box = driver.find_element(By.ID,"APjFqb")
search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
search_box.send_keys("New Horizon")
search_box.submit()
time.sleep(3)
driver.close()
print("Closing your chrome browser!!!!")