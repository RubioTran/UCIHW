import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests

## Step 1 - Scraping

### NASA Mars News

def init_browser():
    excutable_path = {'executable_path': 'chromedriver'}
    return Browser("chrome", headless=False)

def scrape():
    browser = init_browser()
    mars_listings = {}

    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find_all(class_="content_title").get_text().strip()
    news_p = soup.find_all(class_="rollover_description_inner").get_text().strip()

    time.sleep(1)

### JPL Mars Space Images - Featured Image

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(image_url)

    html = browser.html

    soup_image = BeautifulSoup(html, 'html.parser')

    browser.click_link_by_partial_text("FULL IMAGE")

    full_img = soup_image.find_all('footer')

    full = full_img[0]
    
    featured_image = full.a['data-fancybox-href']

    main_url = 'https://www.jpl.nasa.gov'
    featured_image_url = main_url + featured_image  
    print(featured_image_url)

    facts_url = "https://space-facts.com/mars/"

    response2 = requests.get(facts_url)

    soup_facts = BeautifulSoup(response2.text, 'html.parser')

    tables = pd.read_html(facts_url)

### Mars Weather

### Mars Facts

### Mars Hemisperes