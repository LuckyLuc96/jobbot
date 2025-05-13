# Jobbot - An automated Job Application Assistant

Jobbot is a program written in Python and using Selenium and is designed to automate the process of applying for jobs on Indeed. It uses the Chrome WebDriver to interact with the web pages, filling out forms and clicking buttons just as a human user would.
Currently the bot must be supervised, because the user is required to answer job questions and to complete captchas.

## See it in action!

[![Jobbot Demonstration](https://markdown-videos-api.jorgenkh.no/url?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D5FQ2L6zbRMc)](https://www.youtube.com/watch?v=5FQ2L6zbRMc)

## Features
- Opens the Indeed website and searches for jobs based on specified criteria.
- Automatically clicks the "Apply now" button and handles the application process.
- Continuously checks for "Continue" or "Submit your application" buttons to complete the application.
- Handles scrolling to ensure elements are in view before interacting with them.
- Includes error handling and cleanup to close the browser after the process is complete.

## Prerequisites to have installed:
1) A linux operating system or the capability to run BASH commands.
2) Python (sudo apt install python3)
3) Selenium (pip install selenium)
4) Chromium browser (Google Chrome may work)

## Setup
1) Install Python and Selenium
2) Run the script (python3 Jobbot.py) and don't enter in search terms in the terminal. Use the opened browser to login to Indeed.com
3) Now close the browser, and start the script again, following the prompts.



## Todo List
- [x] Allow user input for job search criteria.
- [ ] Make a UI
- [ ] Implement Docker container for easier deployment.
- [ ] Improve error handling and logging.


## License
This project is licensed under the MIT License.

---

Jobbot - a program to make job applications easier.
Created by [Christian McCrea](https://github.com/LuckyLuc96).
