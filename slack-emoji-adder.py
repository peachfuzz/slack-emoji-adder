from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import json

# get credendials from the json file
# either rename the creds-template.json file to creds.json or change this line to say creds-template.json
with open('creds.json') as json_data_file:
    data = json.load(json_data_file)

# set your credentials and workspace here so your username and password isn't inline code :)
username = data["username"]
password = data["password"]
workspace = data["workspace"] + "/customize/emoji"

# the driver isn't working and idk why
# already tried (per: https://www.dev2qa.com/how-to-resolve-webdriverexception-geckodriver-executable-needs-to-be-in-path/):
# brew install geckodriver #installed geckodriver
# geckodriver --version    #verified it was installed
# which geckodriver        #verified it was in my path
# 🤷‍♀️
# driver = webdriver.Firefox()
# # driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
# driver.get(workspace)

# try:
#     wait = WebDriverWait(driver, 10)
#     wait.until(lambda driver: driver.current_url !=
#                "https://comparchwi19.slack.com/customize/emoji")
# finally:
#     driver.quit()
