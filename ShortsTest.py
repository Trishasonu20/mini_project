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

    with allure.step("Open Shorts"):
        driver.get("https://www.youtube.com/shorts/")
        time.sleep(5)

    with allure.step("Close browser"):
        driver.close()

