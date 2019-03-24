from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import json
from selenium.webdriver.common.proxy import *

# get credendials from the json file
# either rename the creds-template.json file to creds.json or change this line to say creds-template.json
with open("creds.json") as json_data_file:
    data = json.load(json_data_file)

# set your credentials and workspace here so your username and password isn't inline code :)
username = data["username"]
password = data["password"]
workspace = data["workspace"] + "/?redir=%2Fcustomize%2Femoji"  # /customize/emoji

# driver = webdriver.Chrome()


firefoxProfile = webdriver.FirefoxProfile()
firefoxProfile.set_preference("permissions.default.stylesheet", 2)
firefoxProfile.set_preference("permissions.default.image", 2)
firefoxProfile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")
firefoxProfile.set_preference("http.response.timeout", 10)
firefoxProfile.set_preference("dom.max_script_run_time", 10)

driver = webdriver.Firefox(firefox_profile=firefoxProfile)
# driver.set_page_load_timeout(10)
driver.get(workspace)

userinput = driver.find_element_by_id("email")
userinput.send_keys(username)

passinput = driver.find_element_by_id("password")
passinput.send_keys(password)
passinput.submit()

# the next page

path = "./emojis"
dirs = os.listdir(path)
for pic in dirs:
    # there needs to be a "wait until page loaded" up here
    driver.findelement
    addcustomemojibutt = driver.find_element_by_class_name(
        "c-button c-button--primary c-button--medium p-customize_emoji_wrapper__custom_button null--primary null--medium"
    )
    addcustomemojibutt.click()

    uploadimagebutt = driver.find_element_by_class_name(
        "c-button c-button--outline c-button--medium null--outline null--medium"
    )
    uploadimagebutt.click(pic)  # hopefully this will be a file

    nameinput = driver.find_element_by_id("emojiname")
    nameinput.send_keys(pic)  # hopefully this will turn into a string

    error = driver.find_element_by_id("c-alert__message")
    # this can be anything....
    if "Please make sure your file is a GIF, JPEG, or PNG." in error.text:
        print("bad file")  # log what file was not an image
    elif "This name is already in use by another emoji." in error.text:
        print("name has already been used bruh")  # possibly rename it??
    else:
        submitbutt = driver.find_element_by_class_name(
            "c-button c-button--primary c-button--medium c-dialog__go null--primary null--medium"
        )  # submit that bishhh

driver.quit()
