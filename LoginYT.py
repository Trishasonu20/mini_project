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
        time.sleep(2)
        driver.get("https://accounts.google.com/v3/signin/identifier?hl=en-gb&ifkv=ATuJsjwsO2kcB8s6lub7i5Z1US-MXHMqBBudb4fy7cXiHH1NqR278ZqZgG-NFgaqjsE-UPu2tgLd3A&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S134969419%3A1710403010860566&theme=mn")
        search =driver.find_element("id","identifierId")
        search.send_keys("bcanhck29@gmail.com")
        search = driver.find_element("xpath","/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]")
        search.click()
    #with allure.step("Login in"):
        #search = driver.find_element("xpath","/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]")
        #search.click()
        #search = driver.find_element("id","identifierId")
        #search.send_keys("")
        #search = driver.find_element("xpath",
                                     #"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
        #search.click()
        #search = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
        #search.send_keys("bcanhck29@gmail.com")


    with allure.step("Close browser"):
        driver.close()

