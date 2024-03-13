import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(1)
search = driver.find_element("name",'search_query')
search.send_keys("beast")
search = driver.find_element("xpath",'//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div')
search.click()
time.sleep(10)

driver.close()