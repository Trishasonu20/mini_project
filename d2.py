from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@allure.severity(allure.severity_level.NORMAL)
class TestGoogleSearch:

    @allure.severity(allure.severity_level.MINOR)
    def test_Google_Search(self):
        self.serv_obj = Service()
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get("https://www.google.com")
        time.sleep(5)
        search_box = self.driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
        search_box.send_keys("hello")
        search_box.submit()
        time.sleep(3)
        self.driver.close()