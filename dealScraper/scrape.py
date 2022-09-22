# pre-existing modules:
import urllib.parse
import json
from time import sleep
from random import randint

# pypi modules:
from selenium import webdriver as wd
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as bs


def formatRequest(params):
    ### URL Formatting Code
    baseURL = 'https://www.amazon.com/gp/goldbox?deals-widget='
    encoded = urllib.parse.quote(json.dumps(params).replace(" ", ""))
    encoded = urllib.parse.quote(encoded)
    absoluteURL = baseURL + encoded
    print(absoluteURL)
    return absoluteURL


def getProducts(absoluteURL):
    ### Web Driver Stuff
    chromeDriverPath = "./chromedriver.exe"
    options = wd.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = wd.Chrome(service=Service(chromeDriverPath), options=options)

    ### Load Dynamic Site, Pass Data to bs4
    driver.get(absoluteURL)
    sleep(randint(3, 5))
    soup = bs(driver.page_source, "html.parser")
    driver.quit()
    return soup


def parser(soup):
    ### Parse Data for Deals
    results = soup.find_all("div", id="slot-15")[1]
    items = results.find_all("h4", class_="a-offscreen")
    links = []
    data = {"Deal0":[], "Deal1":[], "Deal2":[], "Deal3":[], "Deal4":[]}
    n = 0

    ### Add name and price data to data object
    for item in items:
        item_data = {"Name":[], "Price":[], "Link":[]}
        if n < 5:
            item_data['Name'] = item.text.split(";")[0]
            item_data['Price'] = item.text.split(";")[1]
            update_item = "Deal" + str(n)
            data[update_item] = item_data
        n+=1

    # Create list of links
    for link in results.select("a[class^='a-link-normal DealLink']"):
        links.append(link.get('href'))

    # Add links to data object
    n = 0
    for link in links:
        if n < 5:

            update_item = "Deal" + str(n)
            data[update_item]['Link'].append(link)
        n+=1
    return data.values()


    #print(data)
    #print(len(items))
