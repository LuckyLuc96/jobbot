from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import FirefoxProfile
import time

profile_path = "/home/lucky1/.mozilla/firefox/zjpezclp.default-release"
geckodriver_path = "/home/lucky1/.cache/selenium/geckodriver/linux64/0.34.0/geckodriver"
options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
driver = webdriver.Firefox(options=options)

driver.get("http://www.python.org/")



#time.sleep(2)
#driver.quit()
