from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import *
import os
import sys
import json
import time


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
time.sleep(1)
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
    time.sleep(1)
    while not addcustomemojibutt:
        try:
            addcustomemojibutt = driver.find_element_by_xpath(
                "//button[text()='Add Custom Emoji']"
            )
            addcustomemojibutt.click()
        except:
            continue

    time.sleep(1)
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

    nameinput = driver.find_element_by_id("emojiname")
    # maybe put all images in hash table and check to see if pic_str is in hash table??
    pic_str = ""
    pic_str = pic.split(".")[0]
    nameinput.send_keys(pic_str)

    attempts = 0
    error = ""
    submitbutt = ""
    while not submitbutt:
        try:
            submitbutt = driver.find_element_by_xpath("//button[text()='Save']")
            time.sleep(1)
            attempts = 0
            while attempts < 10:
                try:
                    error = driver.find_element_by_class_name("c-alert__message").text
                    # this can be anything....
                    if "Please make sure your file is a GIF, JPEG, or PNG." in error:
                        print("bad file")  # log what file was not an image
                        driver.find_element_by_class_name("c-dialog__close").click()
                        break
                    elif "This name is already in use by another emoji." in error:
                        print(
                            pic_str + " name has already been used bruh"
                        )  # possibly rename it??
                        driver.find_element_by_class_name("c-dialog__close").click()
                        break
                    elif "taken" in error:
                        driver.find_element_by_class_name(
                            "c-dialog__close"
                        ).click()  # already in use by existing emoji
                        break
                    elif not error:
                        print(error + ": " + pic_str)
                        driver.find_element_by_class_name(
                            "c-dialog__close"
                        ).click()  # already in use by existing emoji
                        break
                    # other errors: "contains surprise"
                except:
                    attempts += 1
                    continue
                error = ""
            submitbutt.click()
        except:
            continue
input()
driver.quit()
