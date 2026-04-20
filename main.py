from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# If chromedriver out of date check here: https://googlechromelabs.github.io/chrome-for-testing/#stable
class Jobbot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--user-data-dir=jobbot_profile/")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        self.options.add_experimental_option("useAutomationExtension", False)

        self.options.binary_location = "/usr/bin/chromium-browser"
        self.driver_service = Service(executable_path="chromedriver-linux64/chromedriver")
        self.driver = webdriver.Chrome(options=self.options, service=self.driver_service)
        self.sleeptime = 5
        self.searchname = ""
        self.searchlocation = ""
        self.num_trys = int()
        self.submission = False

        self.resume = ""
        self.resume_selection = 2
        self.captcha = "//iframe[@width='304' and @height='78' and contains(@name, 'a-') and contains(@src, 'recaptcha/enterprise/anchor')]"
        self.captcha2 = "//title[contains(text(), 'Security Check - Indeed.com')]"
        self.completed_path = "//h1[normalize-space(text())='Your application has been submitted!' or normalize-space(text())='Complete a test to help your application stand out' or normalize-space(text())='... share an assessment?']" #Find the missing value for this 3rd option
        self.review_path = "//button[contains(span/text(), 'Review your application') or //h1[normalize-space(text())='Answer these questions from the employer']]"
        self.submit_path = "//button[contains(span/text(), 'Submit your application')]"
        self.continue_path = "//button[contains(span/text(), 'Continue')]"
        self.xpaths = [self.resume, self.review_path, self.captcha, self.completed_path, self.continue_path, self.submit_path]
        self.combined_paths = " | ".join(self.xpaths)

def ensure_visible(self, function):
    @wraps(function)
    def wrapper(driver, element, *args, **kwargs):
        driver.execute_script("""
            var element = arguments[0];
            element.style.display = 'block';
            element.style.visibility = 'visible';
            element.style.opacity = 1;
        """, element)
        return function(driver, element, *args, **kwargs)
    return wrapper

def scroll_into_view(self, driver, element):
    time.sleep(0.1)
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.1)
    self.ensure_visible(element)
def click_element(self, driver, element):
    element.click()

def check_apply_button(self, driver, xpath):
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except TimeoutException:
        return False

def check_element(self):
    try:
        WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.XPATH, self.combined_paths)))
        for xpath in self.xpaths:
            try:
                self.match = self.driver.find_element(By.XPATH, xpath)
                return xpath
            except:
                continue
    except:
        pass

def submission_complete(self):
    self.submission = False
    self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])
    self.driver.refresh()
    time.sleep(self.sleeptime)

def start(self):
    #Search items will become user inputs after testing is finished
    self.searchname = input(str("Type in a job title you are looking for, such as: administrative assistant\n"))
    self.searchlocation = input(str("Type in a job location you are looking for, such as: Remote, USA\n"))
    self.num_trys = int(input("How many applications would you like to attempt?\n"))
    logging.info(f"Starting up. Various parts of the process will wait {self.sleeptime} seconds between actions.")
    self.driver.get("http://www.indeed.com/")
    logging.info("Website opened: ", self.driver.title)

def jobsearch(self):
    self.search_title = self.driver.find_element(By.ID, "text-input-what")
    self.search_location = self.driver.find_element(By.ID, "text-input-where")
    self.search_title.clear()
    time.sleep(2)
    for char in self.searchname:
        self.search_title.send_keys(char)
        time.sleep(0.09)
        self.search_location.clear()
    for char in self.searchlocation:
        self.search_location.send_keys(char)
        time.sleep(0.09)
    self.search_location.send_keys(Keys.RETURN)
    logging.info(f"Search of {self.searchname} with the location set to {self.searchlocation}")
    time.sleep(1)

def captchacheck(self):
    self.match = self.check_element()
    if self.match == self.captcha:
        logging.info("Captcha detected! Please complete this captcha to continue. Resuming in 15 seconds")
        time.sleep(15)
        self.match = self.check_element()
        pass

def mainloop():
    start()
    counter = 0
    while counter < self.num_trys:
        jobsearch()
        captchacheck()
        # Call Indeed.py for now here
        counter = self.counter + 1
        logging.info(f"There are {self.num_trys - self.counter} attempts remaining.")

try:
    mainloop()
except Exception as e:
    logging.info(f"There has been an error. See: {e}")

finally:
    program.driver.quit()
    logging.info("Browser closed!")
