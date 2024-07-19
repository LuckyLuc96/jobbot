from profilenames import profile_path, geckodriver_path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
#options.add_argument("--headless")
driver_service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, service = driver_service)


# This function will read the xpaths available on the application page and continue down a specific path..
# depending on if "submit" or "continue" buttons are available.
def check_element(driver, xpath):
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False

# I had an error with the element being in view, but still saying it was not clickable.
# This function exists to move the viewport directly to where the element is
def scroll_into_view(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print(f"{element} has been scrolled into view!")


try:
    sleeptime = 5 #will make this a user input to add a variable and safe delay on new page loading.
    #int(input("How slow is the internet today? In seconds: \n"))
    print(f"Okay, great! Starting up. Some parts of the program will wait {sleeptime} seconds to load.")
    print("For now this program is still being made, but it is planned to be ran in 'headless' mode which means you won't see the actual browser window.")

    driver.get("http://www.indeed.com/")
    print("Website opened: ", driver.title)

    search_title = driver.find_element(By.ID, "text-input-what")
    search_location = driver.find_element(By.ID, "text-input-where")

    #Replace these two values with the search terms you prefer.
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
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and text()='Apply now' and not(ancestor::*[@aria-label='Apply now (opens in a new tab)'])]"))
    )
    print("Apply button found!:",apply_button.get_attribute('innerHTML'))
    driver.execute_script("arguments[0].scrollIntoView(true);", apply_button)
    time.sleep(3)
    apply_button.click()
    print("Apply button clicked!")
    time.sleep(sleeptime)
    driver.switch_to.window(driver.window_handles[1])
    print("Focusing on newly opened tab..")
    resume_selection = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Indeed Resume']"))
    )
    print("Resume selection button found!:",resume_selection.get_attribute('innerHTML'))
    resume_selection.click()
    print("Resume selected!")
    time.sleep(2)


    submission = False
    while not submission:
        continue_path = "//button[contains(span/text(), 'Continue')]"
        submit_path = "//button[contains(span/text(), 'Submit your application')]"
        print("This is inside of the while loop, but before any arguments are passed.")
        if check_element(driver, continue_path):
            print("continue_path taken")
            continue_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Continue')]"))
            )
            print("Continue button found!", continue_button.get_attribute('innerHTML'))
            scroll_into_view(driver, continue_button)
            time.sleep(3)
            continue_button.click()
            print("Continue button selected!")
            print(f"Waiting {sleeptime} seconds.")
            time.sleep(sleeptime)

        elif check_element(driver, submit_path):
            print("submit_path taken")
            submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(span/text(), 'Submit your application')]"))
            )
            print("Submit button found!", submit_button.get_attribute('innerHTML'))
            driver.execute_script("arguments[0].scrollIntoView();", submit_button)
            time.sleep(5)
            submit_button.click()
            print("Submit button selected!")
            print(f"Waiting {sleeptime} seconds.")
            time.sleep(sleeptime)
            submission = True
        else:
            print("Element not found. Exiting..")
            submission = True




except Exception as e:
    print("There has been an error. See: ", e)
    time.sleep(5)

finally:
    driver.quit()
    print("Browser closed!")





#MIT License
#
#Copyright (c) [2024] [Christian McCrea]
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
