import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
search = driver.get("https://www.youtube.com/shorts/")
time.sleep(10)
driver.close()
