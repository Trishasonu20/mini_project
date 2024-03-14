import time
import allure
from selenium import webdriver

@allure.feature("Home Page Open Feature")
@allure.story("Open Home Page")
@allure.title("Test Home Page Functionality")
def test_post():
    with allure.step("Open browser"):
        driver = webdriver.Firefox()
        driver.get("https://www.youtube.com//")
        time.sleep(10)

    with allure.step("Close browser"):
        driver.close()