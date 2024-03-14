import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
search = driver.get("https://www.youtube.com/feed/trending?bp=6gQJRkVleHBsb3Jl")
time.sleep(5)
driver.close()
