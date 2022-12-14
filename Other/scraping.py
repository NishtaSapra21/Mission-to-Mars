# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt
import requests


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres":hemisphere_images(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first <a> tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def hemisphere_images(browser):
    #Use browser to visit the URL 
    #url = 'https://marshemispheres.com/'
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url)

    # Parse the resulting html with soup
    html = browser.html
    hemisphere_img_soup = soup(html, 'html.parser')
    
    # 2. Create a list to hold the images and titles.

    new_url = 'https://astrogeology.usgs.gov'

    hemisphere_image_urls= []

    image_urls = hemisphere_img_soup.find_all('a', class_='itemLink product-item', href=True)

    hemi_image_urls = []
    for link in image_urls:
        hemi_img_url = f'{new_url}{link["href"]}'
        if hemi_img_url not in hemi_image_urls : 
            hemi_image_urls.append(hemi_img_url) 
        

    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    

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

    return hemisphere_image_urls
