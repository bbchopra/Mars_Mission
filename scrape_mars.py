# Import Dependecies 
from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 

# Initialize browser
def init_browser(): 
    exec_path = {'executable_path': 'chromedriver'}
    return Browser('chrome', **exec_path, headless=True)

# Global dictionary that can be imported into Mongo
mars_info = {}

def scrape():
    # Initialize browser 
    browser = init_browser()

    #-----------------------------------------------------------#
    # NASA MARS NEWS
    # Visit Nasa news url through splinter module
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve the latest element that contains news title and news_paragraph
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # save title and news info
    mars_info['news_title'] = news_title
    mars_info['news_paragraph'] = news_p
    
    #-----------------------------------------------------------#
    # FEATURED IMAGE
    # Visit Mars Space Images through splinter module
    image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url_featured)# Visit Mars Space Images through splinter module

    # HTML Object 
    html_image = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_image, 'html.parser')

    # Retrieve background-image url from style tag 
    image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

    # Website Url 
    main_url = 'https://www.jpl.nasa.gov'

    # Concatenate website url with scrapped route
    featured_image_url = main_url + image_url

    # Display full link to featured image
    featured_image_url 

    # save the image url
    mars_info['featured_image_url'] = featured_image_url 

    #----------------------------------------------------------------#
    # Mars Weather 
    # Visit Mars Weather Twitter through splinter module
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)

    # HTML Object 
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_weather, 'html.parser')

    # Find all elements that contain tweets
    tweet_pic = soup.find('div', 'p', class_='js-tweet-text-container').find('a').text
    weather_tweet = soup.find('div', 'p', class_='js-tweet-text-container').text.replace(tweet_pic,"")

    # save the tweet
    mars_info['weather_tweet'] = weather_tweet

    #----------------------------------------------------------------#
    # Mars Facts
    # Visit Mars facts url 
    facts_url = 'http://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    mars_facts = pd.read_html(facts_url)

    # Find the mars facts DataFrame in the list of DataFrames as assign it to `mars_df`
    mars_df = mars_facts[0]

    # Assign the columns `['Description', 'Value']`
    mars_df.columns = ['Description','Value']

    # Set the index to the `Description` column without row indexing
    mars_df.set_index('Description', inplace=True)

    # Save html code to folder Assets
    data = mars_df.to_html()

    # save the data
    mars_info['mars_facts'] = data

    #--------------------------------------------------#
    # MARS HEMISPHERES
    # Visit hemispheres website through splinter module 
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemispheres_url)

    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    items = soup.find_all('div', class_='item')

    # Create empty list for hemisphere urls 
    hemisphere_image_url = []

    # Store the main_ul 
    hemispheres_main_url = 'https://astrogeology.usgs.gov' 

    # Loop through the items previously stored
    for item in items: 
        # Store title
        title = item.find('h3').text

        # Store link that leads to full image website
        partial_img_url = item.find('a', class_='itemLink product-item')['href']

        # Visit the link that contains the full image website 
        browser.visit(hemispheres_main_url + partial_img_url)

        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html

        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        soup = BeautifulSoup( partial_img_html, 'html.parser')

        # Retrieve full image source 
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']

        # Append the retreived information into a list of dictionaries 
        hemisphere_image_url.append({"title" : title, "img_url" : img_url})
    #save the urls
    mars_info['hiu'] = hemisphere_image_url


    browser.quit()

    # return mars dictionary 
    return mars_info
