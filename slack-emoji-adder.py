from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import json

# get credendials from the json file 
with open('creds.json') as json_data_file: # either rename the creds-template.json file to creds.json or change this line to say creds-template.json
    data = json.load(json_data_file)

# set your credentials here so your username and password isn't inline code :)
username = data["username"]
password = data["password"]

wait = WebDriverWait(driver, 10)
wait.until(lambda driver: driver.current_url != "https://comparchwi19.slack.com/customize/emoji")

# driver = webdriver.Chrome()
# driver.get("https://comparchwi19.slack.com/customize/emoji")