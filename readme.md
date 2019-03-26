#Slack Emoji Adder
This script should use your slack credentials and slack workspace to automatically create emojis from images in a desired folder.

#Requirements
You will need selenium.
Install it with:

```bash
pip install selenium
```

You will need to have driver for Chrome.
Install it with:

```bash
brew install chromedriver
```

Then simply put your images in the "emojis" folder. The program will attempt to upload all of the file that are in the emojis folder.

If you are having issues with chromedriver/geckodriver connecting to the lan, go to this link: https://stackoverflow.com/questions/48824322/unable-to-run-the-selenium-script-while-connected-to-the-lan

You may also be having hosting issues like I did. Go to this link: http://osxdaily.com/2014/04/12/restore-original-hosts-file-mac/
