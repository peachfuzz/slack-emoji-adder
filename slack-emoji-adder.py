from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
import os
import sys
import json


# get credendials from the json file
# either rename the creds-template.json file to creds.json or change this line to say creds-template.json
with open("creds.json") as json_data_file:
    data = json.load(json_data_file)

# set your credentials and workspace here so your username and password isn't inline code :)
username = data["username"]
password = data["password"]
workspace = data["workspace"] + "/?redir=%2Fcustomize%2Femoji"  # /customize/emoji

driver = webdriver.Chrome()
# driver = webdriver.Firefox()

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
    addcustomemojibutt = ""
    while not addcustomemojibutt:
        try:
            addcustomemojibutt = driver.find_element_by_xpath(
                "//button[text()='Add Custom Emoji']"
            )
            addcustomemojibutt.click()
        except:
            continue
    addcustomemojibutt = ""

    uploadimageinput = ""
    temp = ""
    while not uploadimageinput:

        try:
            uploadimageinput = driver.find_element_by_id("emojiimg")
            temp = os.getcwd() + "/emojis/" + pic
            temp = temp.replace("\\", "/")
            uploadimageinput.send_keys(temp)

        except:
            continue

    uploadimageinput = ""
    temp = ""

    nameinput = driver.find_element_by_id("emojiname")
    # maybe put all images in hash table and check to see if pic_str is in hash table??
    pic_str = ""
    pic_str = pic.split(".")[0]
    nameinput.send_keys(pic_str)
    pic_str = ""
    attempts = 0
    error = ""
    while attempts < 10:
        try:
            error = driver.find_element_by_id("c-alert__message")
            # this can be anything....
            if "Please make sure your file is a GIF, JPEG, or PNG." in error.text:
                print("bad file")  # log what file was not an image
            elif "This name is already in use by another emoji." in error.text:
                print("name has already been used bruh")  # possibly rename it??
        except:
            attempts += 1
            continue
    error = ""
    submitbutt = ""
    while not submitbutt:
        try:
            # submitbutt = driver.find_element_by_class_name(
            #     "c-button c-button--primary c-button--medium c-dialog__go null--primary null--medium"
            # )  # submit that bishhh
            submitbutt = driver.find_element_by_xpath("//button[text()='Save']")
            submitbutt.click()
        except:
            continue
    submitbutt = ""
input()
driver.quit()
