# MIT License
# Jobbot - a program to make job applications easier.
# Copyright (c) [2024] [Christian McCrea]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
from functools import wraps

options = webdriver.FirefoxOptions()
options.profile = webdriver.FirefoxProfile(profile_path)
#options.add_argument("--headless")
driver_service = Service(executable_path=geckodriver_path)
driver = webdriver.Firefox(options=options, service = driver_service)

# Function wrapper to ensure that a element on the page is actually visible to the bot
def ensure_visible(func):
    @wraps(func)
    def wrapper(driver, element, *args, **kwargs):
        driver.execute_script("""
            var element = arguments[0];
            element.style.display = 'block';
            element.style.visibility = 'visible';
            element.style.opacity = 1;
        """, element)
        return func(driver, element, *args, **kwargs)
    return wrapper

# This function will read the xpaths available on the application page and continue down a specific path..
# depending on if "submit" or "continue" buttons are available.


def check_apply_button(driver, xpath):
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False

# This function exists to move the viewport directly to where the element is
def scroll_into_view(driver, element):
    time.sleep(0.25)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.25)
@ensure_visible
def click_element(driver, element):
    element.click()

def init():
    global sleeptime
    global searchname
    global searchlocation
    global num_trys
    sleeptime = 5
    #Search items will become user inputs after testing is finished
    searchname = input(str("Type in a job title you are looking for, such as: administrative assistant\n"))
    searchlocation = input(str("Type in a job location you are looking for, such as: Remote, USA\n"))
    num_trys = int(input("How many applications would you like to attempt?\n"))
    print(f"Starting up. Various parts of the process will wait {sleeptime} seconds between actions.")

    driver.get("http://www.indeed.com/")
    print("Website opened: ", driver.title)

def jobsearch():
    search_title = driver.find_element(By.ID, "text-input-what")
    search_location = driver.find_element(By.ID, "text-input-where")
    search_title.clear()
    search_title.send_keys(searchname)
    search_location.clear()
    search_location.send_keys(searchlocation)
    search_location.send_keys(Keys.RETURN)
    print(f"Search of {searchname} with the location set to {searchlocation}")
    time.sleep(1)

def main():
    time.sleep(sleeptime)
    jobtitles = driver.find_elements(By.XPATH, '//*[contains(@class, "jcs-JobTitle")]')
    for item in jobtitles:
        scroll_into_view(driver, item)
        click_element(driver, item)
        print("Searching for an on-site application..")
        apply_button = check_apply_button(driver, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and contains (text(),'Apply now') and not (ancestor::*[@aria-label='Apply now (opens in a new  tab)'])]")
        if apply_button:
            apply_button = WebDriverWait(driver, sleeptime).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and contains (text(),'Apply now') and not (ancestor::*[@aria-label='Apply now (opens in a new  tab)'])]")))
            print("Eligible application found!")
            time.sleep(3)
            apply_button.click()
            break
        else:
            print("This job is offsite. Lets try another one..")
            continue


    time.sleep(1.5)
    driver.switch_to.window(driver.window_handles[1])
    print("Focusing on newly opened tab..")
    time.sleep(sleeptime)



    submission = False
    def submission_complete():
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.refresh()
        time.sleep(sleeptime)
        submission = True

    while not submission:

        captcha = "//iframe[@width='304' and @height='78' and contains(@name, 'a-') and contains(@src, 'recaptcha/enterprise/anchor')]"
        completed_path = "//h1[normalize-space(text())='Your application has been submitted!' or normalize-space(text())='Complete a test to help your application stand out' or normalize-space(text())='... share an assessment?']" #Find the missing value for this 3rd option
        review_path = "//button[contains(span/text(), 'Review your application') or //h1[normalize-space(text())='Answer these questions from the employer']]"
        submit_path = "//button[contains(span/text(), 'Submit your application')]"
        continue_path = "//button[contains(span/text(), 'Continue')]"

        #Following logic is made to reduce search time on a page to decide what to do next. Instead of searching each element individually, it will search for all of the elements I am looking for. When one is found, it will then execute the related commands for that element.
        xpaths = [review_path, captcha, completed_path, continue_path, submit_path]
        combined_paths = " | ".join(xpaths)

        def check_element():
            try:
                WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, combined_paths)))
                for xpath in xpaths:
                    try:
                        match = driver.find_element(By.XPATH, xpath)
                        return xpath
                    except:
                        continue
            except:
                pass
        match = check_element()

        if match == review_path:
            print("Answer the questions on this page and progress to the next page. The program will detect when this is done.\nWaiting 10 seconds.")
            time.sleep(10)
            #TODO: Fill in some questions programatically. This is going to require the user to provide the answers to these questions within the program when they set it up so that they are unique to the user. These answers will be added to and then extracted from profiles.py, which will probably be renamed to settings.py.

        elif match == continue_path:
            continue_button = WebDriverWait(driver, sleeptime).until(EC.presence_of_element_located((By.XPATH, continue_path)))
            scroll_into_view(driver, continue_button)
            click_element(driver, continue_button)
            print("Continue button selected!")
            time.sleep(sleeptime)

        elif match == captcha:
            print("Captcha detected! Please complete it and then hit the submit button. The program will continue in 10 seconds..")
            time.sleep(10)
            continue

        elif match == completed_path:
            print("Application completed!")
            submission_complete()

        elif match == submit_path:
            submit_button = WebDriverWait(driver, sleeptime).until (EC.presence_of_element_located((By.XPATH, submit_path)))
            scroll_into_view(driver, submit_button)
            time.sleep(2)
            submit_button.click()
            print("Application submitted!")
            time.sleep(2)
            submission_complete()

        else:
            print("None of the expected elements were found!")
            break

try:
    init()
    counter = 0
    while counter < num_trys:
        jobsearch()
        main()
        counter = counter + 1
        print(f"There are {num_trys - counter} attempts remaining.")

except Exception as e:
    print("There has been an error. See: ", e)

finally:
    driver.quit()
    print("Browser closed!")
