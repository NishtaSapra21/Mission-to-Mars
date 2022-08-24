# Mission to Mars

## Purpose

This analysis automates a web browser to visit different websites to extract data of __Mars__ and its __Hemispheres’  Full Size Images__  with __“Splinter”__ and __”BeautifulSoup”__  and stores it in a NoSQL database , i.e __“MongoDB__ , and then renders the data in a web application (using __HTML, CSS__ ) created with __Flask__ . 

## Result

We can divide this web scrapping in four steps: web scrapping , store data in database, display the data, customize the data. Let’s have a brief look of each step. 

1. __Web Scrapping with Splinter and BeutifulSoup__

    In this step BeautifulSoup and Splinter automate Chrome browser  to visit the __https://marshemispheres.com/__ or 
    __https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars__ . After inspecting the page and finding data to extract, HTML parser           parses the data. Code is written to extract desired     data and stored them in required format. Here, we are retrieving full resolution image url for each Mars’s     hemispheres and title from parsed HTML data and saving       image url and image title in dictionary and finally saving dictionary data into a list. All  code is       written in __Mission_to_Mars_Challenge.ipynb__  file. 
    
    following imagesshows a list of image urls and image titles using https://marshemispheres.com/ and              
    https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars.
    
    The "Other" folder saves all files need to scrap data from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars and web display. 
    
    ![url_title1](https://user-images.githubusercontent.com/107717882/186522450-447566ed-c433-479c-b7fa-8e037469cfbf.png)

    ![url_title2](https://user-images.githubusercontent.com/107717882/186522479-8c873d33-a6b4-46d8-8f9e-f46121008fc9.png)


2. __Store Data in MongoDB Database__

    In this step, __scrapping.py__ file has been created with all necessary function to scrap data. Code has been used from __Mission_to_Mars_Challenge.ipynb__ .           A new file called __app.py__  is created to import  __Flask__  and __MongoDB__ dependencies and ofcourse, our __scapping.py__  file too. First, the                     desired data is stored in MongoDB database __mars_app__. Next, the  __render_template()__ function of Flask communicates with HTML file (index,html) and MongoDB       database to data and generates a dynamic web-page contents.

    The app.py file calls scrapping functions and stores our __hemispheres' urls and titles__ in MongoDB __mars_app__ database with other information. It also passes       that info to our __index.html__ file to display. 
    
    Hvea a look at __mars_app__ dtabase structure in MongoDB.
    
    ![mongodb_data](https://user-images.githubusercontent.com/107717882/186522537-d14618e5-7424-4d7d-9f78-ff190d52223b.png)


3. __Display Data with Flask Application__ 

    After running our flask application using __python app.py__ command on anaconda prompt, Flask interacts with both HTML and MongoDB to display web page. 

    After copying address __http://127.0.0.1:5000/__ from Flask run output and paste it in our browser, our local host will run our new designed web page with all four     mars hemispheres full images and of course, other data too. 
    
    See the all four hemispheres full images display using Bootsrap's __col-md-6__ grid class. 
    
    ![mars_hemispheres_full_images](https://user-images.githubusercontent.com/107717882/186522581-1dcd0af4-af84-404a-b118-7be92fc26a1b.png)


4. __Customize Display with HTML/CSS and Bootstrap Components__

    The “index.html” file, using HTML tags and using __CSS__ file decides how and where display the data/contents in user friendly, nice format. 
    
    Our final web page with all updates of __index.html__ and __style.css__ .
    
    ![web_page](https://user-images.githubusercontent.com/107717882/186522631-9dca3c91-679a-4cff-99fc-c14ec7cd5aa7.png)


## Summary

Web scraping automates the browser to collect data that we want and makes the things easy and simplified. There’s knowledge of HTML tags helps to find and extract data.  But you should  always check that the website you want to scrape allows users to scrap data or not. 
There’s a beautiful webpage displaying  information about mars with all four hemispheres images above.
