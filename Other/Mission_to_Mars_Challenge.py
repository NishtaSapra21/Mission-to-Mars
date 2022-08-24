#!/usr/bin/env python
# coding: utf-8

# ### Module 10 Challenge Code 


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# ### Visit the Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
#url = 'https://marshemispheres.com/'

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

browser.visit(url)

# Parse the resulting html with soup
html = browser.html
hemisphere_img_soup = soup(html, 'html.parser')
hemisphere_img_soup


# 2. Create a list to hold the images and titles.

new_url = 'https://astrogeology.usgs.gov'

hemisphere_image_urls= []

image_urls = hemisphere_img_soup.find_all('a', class_='itemLink product-item', href=True)

hemi_image_urls = []
for link in image_urls:
    hemi_img_url = f'{new_url}{link["href"]}'
    if hemi_img_url not in hemi_image_urls : 
        hemi_image_urls.append(hemi_img_url) 
        
print(len(hemi_image_urls))
hemi_image_urls

# 3. Write code to retrieve the image urls and titles for each hemisphere.
import requests


for i in range(4):
    
    # request for HTML document of given url
    response = requests.get(hemi_image_urls[i])      
    # response will be provided in JSON format
    img_page = response.text

    img_soup = soup(img_page, 'html.parser')

    # Scrape the Image Title 
    img_title = img_soup.find('h2', class_='title')
    if img_title is not None:
            text = img_title.get_text()
            img_title = text
    print(img_title)

    # Scrape the Image Link 
    img_url = img_soup.find('a',text='Sample', href=True)
    if img_url is not None:    
        img_url = f'{img_url["href"]}'
    print(img_url)

    # Define and append to the dictionary
    hemispheres = {}
    hemispheres['img_url'] = img_url
    hemispheres['title'] = img_title
    
    # Append to the List
    hemisphere_image_urls.append(hemispheres)
    
    # Browse Back
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()

