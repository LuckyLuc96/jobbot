from profilenames import profile_path, geckodriver_path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
driver_service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, service = driver_service)


driver.get("http://www.indeed.com/")
print("Website opened: ", driver.title)
try:
    search_title = driver.find_element(By.ID, "text-input-what")
    search_location = driver.find_element(By.ID, "text-input-where")

    searchname = "administrative"
    searchlocation = "remote"
    search_title.clear()
    search_title.send_keys(searchname)
    search_location.clear()
    search_location.send_keys(searchlocation)
    search_location.send_keys(Keys.RETURN)
    print(f"Search of {searchname} with the location set to {searchlocation}")
    time.sleep(3)
    apply_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and text()='Apply now' and not(@aria-label='Apply now (opens in a new tab)')]"))
    )
    # These are the actions of clicking the above buttons
    apply_button.click()
    time.sleep(4)
    resume_selection = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Indeed Resume']"))
    )
    continue_button = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Continue']"))
    )
    resume_selection.click()
    time.sleep(0.5)
    continue_button.click()
    time.sleep(3)
    continue_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Continue']"))
    )
    continue_button2.click()
    time.sleep(3)





except Exception as e:
    print("There has been an error. See: ", e)

finally:
    time.sleep(10)
    driver.quit()
    print("Browser closed!")
