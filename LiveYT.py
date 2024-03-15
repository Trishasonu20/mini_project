import time
import allure
from selenium import webdriver

@allure.feature("Search Open Feature")
@allure.story("Search Feature")
@allure.title("Test Search Functionality")
def test_post():
    with allure.step("Open browser"):
        driver = webdriver.Firefox()
        driver.get("https://www.youtube.com//")
        time.sleep(10)

        search = driver.find_element("name", 'search_query')
        search.send_keys("beast")
        search = driver.find_element("xpath", '//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div')
        search.click()
        time.sleep(5)

        time.sleep(5)

    with allure.step("Close browser"):
        driver.close()

