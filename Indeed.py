def main(self):
    time.sleep(self.sleeptime)
    self.jobtitles = self.driver.find_elements(By.XPATH, '//*[contains(@class, "jcs-JobTitle")]')
    for item in self.jobtitles:
        self.scroll_into_view(self.driver, item)
        self.click_element(self.driver, item)
        logging.info("Searching for an on-site application..")
        self.apply_button = self.check_apply_button(self.driver, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and contains (text(),'Apply now') and not (ancestor::*[@aria-label='Apply now (opens in a new  tab)'])]")
        if self.apply_button:
            self.apply_button = WebDriverWait(self.driver, self.sleeptime).until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'jobsearch-IndeedApplyButton-newDesign') and contains (text(),'Apply now') and not (ancestor::*[@aria-label='Apply now (opens in a  new  tab)'])]")))
            logging.info("Eligible application found!")
            time.sleep(1.5)
            self.apply_button.click()
            break
        else:
            logging.info("This job is offsite. Lets try another one..")
            continue

    self.driver.switch_to.window(self.driver.window_handles[1])
    logging.info("Focusing on newly opened tab..")
    time.sleep(self.sleeptime)

    while not self.submission:
        if self.resume_selection == 1:
            self.resume = "//span[text()='Indeed Resume']" #Indeed's resume
            if self.resume_selection == 2:
                self.resume = "//label[@data-testid='FileResumeCard-label']" #User uploaded resume
        self.match = self.check_element()
        if self.match == self.resume:
            self.resume_button = WebDriverWait(self.driver, self.sleeptime).until(EC.presence_of_element_located((By.XPATH, self.resume)))
            self.continue_button = WebDriverWait(self.driver, self.sleeptime).until(EC.presence_of_element_located((By.XPATH, self.continue_path)))
            self.scroll_into_view(self.driver, self.resume_button)
            self.click_element(self.driver, self.resume_button)
            time.sleep(1.5)
            self.scroll_into_view(self.driver, self.continue_button)
            self.click_element(self.driver, self.continue_button)
            logging.info("Continue button selected!")
            time.sleep(self.sleeptime)
        elif self.match == self.review_path:
            logging.info("Answer the questions on this page and progress to the next page. The program will detect when this is done.\nWaiting 10 seconds.")
            time.sleep(10)
            #TODO: Fill in some questions programatically. This is going to require the user to provide the answers to these questions within the program when they set it up so that   they are unique to the user. These answers will be added to and then extracted from profiles.py, which will probably be renamed to settings.py.
        elif self.match == self.continue_path:
            self.continue_button = WebDriverWait(self.driver, self.sleeptime).until(EC.presence_of_element_located((By.XPATH, self.continue_path)))
            self.scroll_into_view(self.driver, self.continue_button)
            self.click_element(self.driver, self.continue_button)
            logging.info("Continue button selected!")
            time.sleep(self.sleeptime)
        elif self.match == self.captcha:
            logging.info("Captcha detected! Please complete it and then hit the submit button. The program will continue in 10 seconds..")
            time.sleep(10)
            continue
        elif self.match == self.completed_path:
            logging.info("Application completed!")
            self.submission = True
            self.submission_complete()
        elif self.match == self.submit_path:
            self.submit_button = WebDriverWait(self.driver, self.sleeptime).until (EC.presence_of_element_located((By.XPATH, self.submit_path)))
            self.scroll_into_view(self.driver, self.submit_button)
            time.sleep(2)
            self.submit_button.click()
            time.sleep(1.5)
            self.submission = True
            self.submission_complete()
        else:
            logging.info("None of the expected elements were found!")
            break