# CRIME LIST SCRAPER
- This is an crime list online scraper using the scrapy framework.
- The content is in table format.
- The link to the website is https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate.
## CREATING THE PROJECT
- To open your new project:
  - Open a directory in you code editor.
  - type 'scrapy startproject crime_list_scraper'.
  - Then 'cd crime_list_scraper' to enter the new directory.
## CREATING A SPIDER
- We now need a spider to help in crawling, to create it we:
  - type 'scrapy genspider crimelistspider https://en.wikipedia.org/wiki/List_of_United_States_cities_by_crime_rate'.
- Open the ebookspider.py file in the spider folder.
## CRAWLING USING THE SPIDER
- To crawl type 'scrapy crawl crimelistspider'
- To save the data in a json format type 'scrapy crawl crimelistspider -O filename.json'
- To save the data in a csv format type 'scrapy crawl crimelistspider -O filename.csv'
