# Mars_Mission
-------------------------------------------------------------------------------------------------------------------------------------------
In this assignment, a web application is built that scrapes data from different websites to gather data related to the "Mission to Mars" and displays the information in a single HTML page.

Scraping websites:
https://mars.nasa.gov/news/ is used to scrape latest news title and news 
https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars is used to scrape the featured image of mars
https://twitter.com/marswxreport?lang=en is used to get the latest tweet on the mars weather.
https://space-facts.com/mars/ is used to gather the facts about Mars
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars is used to get the Mars hemispheres images

Flask:
A python script to run all of the scraping code is designed and all of the scraped data is put into one Python dictionary.
'/scrape' route is used to import the Python script and call the scrape function created.

MongoDB:
A new database and a new collection is created to store all the scraped data.

HTML and BootStrap:
A HTML file 'index.html' iss created that displaysall of the data in HTML elements.

To run the application,
1. Execute "Python app.py" in GitBash 
   -> When "Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)", is shown in the GitBash window, this means the application started
2. Go to Chrome browser and visit the URL : http://localhost:5000/
3. To scrape latest info, click "Scrape New Data"
4. The updated website is shown

