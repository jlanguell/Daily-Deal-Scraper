# pre-existing modules:
import urllib.parse
import json
from time import sleep
from random import randint

# pypi modules:
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs

### Web Driver Stuff
chromeDriverPath = "./chromedriver.exe"
options = wd.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = wd.Chrome(service=Service(chromeDriverPath), options=options)

params = {
              "version":1,
              "viewIndex":0,
              "presetId":"910CF237E56A78E679CC73E3ED11EA79",
              "prime":True,
              "departments":["283155"],
              "sorting":"BY_CUSTOM_CRITERION",
              "starRating":4

}

### URL Formatting Code
baseURL = 'https://www.amazon.com/gp/goldbox?deals-widget='
encoded = urllib.parse.quote(json.dumps(params).replace(" ", ""))
encoded = urllib.parse.quote(encoded)
absoluteURL = baseURL + encoded

### Load Dynamic Site, Pass Data to bs4
driver.get(absoluteURL)
sleep(randint(3, 5))
soup = bs(driver.page_source, "lxml")
driver.quit()

### Parse Data for Deals
results = soup.find_all("div", id="slot-15")[1]
items = results.find_all("h4", class_="a-offscreen")


### Test code to display information
for item in items:
    print(item.text)
print(len(items))

