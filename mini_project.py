import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(1)
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252Ffeed%252Fsubscriptions&ec=65620&hl=en&ifkv=ATuJsjwf0_Cg8jf22CAetQgDhjdCIWl9QFLYGBMn3uaBT4ScEbhgmKjrh7XV5G9thXuw4Slxo0ovDQ&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1175024405%3A1710391801588122&theme=mn")
search = driver.find_element("xpath",'//*[@id="identifierId"]')

search.send_keys("deepakdk212204@gmail.com")
time.sleep(2)
search =driver.find_element("xpath", '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/div[3]')
search.click()
#search = driver.find_element("xpath",'//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div')
search.click()
time.sleep(10)

driver.close()
