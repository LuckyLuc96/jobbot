from profilenames import profile_path, geckodriver_path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import FirefoxProfile
import time


options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
driver_service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, service = driver_service) #options(or profile name) is correcct. The gecko driver is not working on the device I'm using right now.


driver.get("http://www.indeed.com/")
print("Website opened: ", driver.title)

search_title = driver.find_element(By.ID, "text-input-what")
search_location = driver.find_element(By.ID, "text-input-where")

search_title.clear()
search_title.send_keys("administrative")
search_location.clear()
search_location.send_keys("Remote")
search_location.send_keys(Keys.RETURN)



time.sleep(3)
driver.quit()

profile_path = "/home/lucky1/.mozilla/firefox/uhc9pf1j.Selenium"
geckodriver_path = "/home/lucky1/.cache/selenium/geckodriver/linux64/0.34.0/geckodriver"
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
driver = webdriver.Firefox(options=options)

driver.get("http://www.indeed.com/")
print("Website opened: ", driver.title)

search_title = driver.find_element(By.ID, "text-input-what")
search_location = driver.find_element(By.ID, "text-input-where")

search_title.clear()
search_title.send_keys("administrative")
search_location.clear()
search_location.send_keys("Remote")
search_location.send_keys(Keys.RETURN)



time.sleep(3)
driver.quit()
