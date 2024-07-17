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


try:
    sleeptime = 10
    #int(input("How slow is the internet today? In seconds: \n"))
    print(f"Okay, great! Starting up. Some parts of the program will wait {sleeptime} seconds to load.")
    print("For now this program is still being made, but it is planned to be ran in 'headless' mode which means you won't see the window.")

    driver.get("http://www.indeed.com/")
    print("Website opened: ", driver.title)

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
    print("Apply button found!:",apply_button.get_attribute('innerHTML'))
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", apply_button)

    apply_button.click()
    print("Apply button clicked!")
    time.sleep(sleeptime)
    driver.switch_to.window(driver.window_handles[1])
    print("Switching selenium to focus on new tab opened by applying")
    resume_selection = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Indeed Resume']"))
    )
    print("Resume selection button found!:",resume_selection.get_attribute('innerHTML'))

    resume_selection.click()
    print("Resume selected!")
    time.sleep(2)
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue')]"))
    )
    print("Continue button found!:",continue_button.get_attribute('innerHTML'))
    if not continue_button.is_displayed(): #Will scroll down to the button, if button is not visible
        driver.execute_script("arguments[0].scrollIntoView();", continue_button)
    time.sleep(1)
    continue_button.click()
    print("continued button selected!")
    print(f"Waiting {sleeptime} seconds.")
    time.sleep(sleeptime)

    #This is where it asks for a relevant job.
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue')]"))
    )
    continue_button.click()
    #This is where it asks employer questions. I suspect the most problems from this section in the future.
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue')]"))
    )
    continue_button.click()
    #This is asking if I have certain qualifications. I should make a loop for this..
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue')]"))
    )
    continue_button.click()

    #This is Indeed saying I am not qualified. Should I continue applying? Of course.
    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue applying')]"))
    )
    if not continue_button.is_displayed(): #Will scroll down to the button, if button is not visible
        driver.execute_script("arguments[0].scrollIntoView();", continue_button)
    continue_button.click()

    #This is where you submit your application!
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Submit your application')]"))
    )
    if not submit_button.is_displayed(): #Will scroll down to the button, if button is not visible
        driver.execute_script("arguments[0].scrollIntoView();", submit_button)
        submit_button.click()



except Exception as e:
    print("There has been an error. See: ", e)
    driver.close()
    time.sleep(5)

finally:
    driver.quit()
    print("Browser closed!")
