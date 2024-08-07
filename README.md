# Jobbot - An automated Job Application Assistant

Jobbot is a program written in Python and using Selenium and is designed to automate the process of applying for jobs on Indeed. It uses the Firefox WebDriver to interact with the web pages, filling out forms and clicking buttons just as a human user would.
Currently the bot must be supervised, because the user is required to answer job questions and to complete captchas.

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
4) Firefox (sudo apt install firefox)

## Setup
0) List of commands without description:
    a) firefox -P
    b) chmod +x setup.sh
    c) ./setup.sh
    d) python3 jobbot.py
1) Set up a new firefox profile so that the program can run that new profile instead of using your main one.
    a) Open a terminal run "firefox -P"
    b) Create a new profile
    c) Log into your Indeed.com account

2) Make setup.sh executable by running the command:"chmod +x setup.sh" Run setup.sh via "./setup.sh" and modify the variables inside the newly created file to fit the file paths to the newly created firefox profile and the firefox geckodriver.
or
2b) Create a file named profilenames.py and then create two variables named profile_path and geckodriver_path. These need to be given the value as a string to the direct path to your newly created firefox profile and the geckodriver respectively. The shellscript names these values to the values that I use as an example of where to look.
3) Run the bot by running the command "python3 jobbot.py"

## Todo List
- [x] Add detailed setup instructions.
- [x] Allow user input for job search criteria.
- [ ] Implement Docker container for easier deployment.
- [ ] Improve error handling and logging.


## License
This project is licensed under the MIT License.

---

Jobbot - a program to make job applications easier.
Created by [Christian McCrea](https://github.com/LuckyLuc96).
