# Houseofindya

Hello This is a python webscraping project using scrapy web scrapper.

        git clone https://github.com/sohamchoudhury18/Houseofindya.git
        cd Houseofindya

website scraped - https://www.houseofindya.com/ 

Data Scrapped from the website are necklace sets from jewellery category 

## Spiders Used
#### [urlspider](https://github.com/sohamchoudhury18/Houseofindya/blob/master/houseofindya/houseofindya/spiders/urlspider.py)
#### [listing_scraper](https://github.com/sohamchoudhury18/Houseofindya/blob/master/houseofindya/houseofindya/spiders/listing_loader.py)

## Usage 
    scrapy crawl urlspider
this will collect all the listing urls for the specified categories ( necklace sets)

    scrapy crawl listing_scraper 
This spider will collect all the listing data and by default store all the information in a csv file with a timestamp 

For paticular file formats such as json please pass a command line argument requesting a json file with a file name

    scrapy crawl listing_scraper -t json -o listing_data.json

##Output files
[URL.csv](https://github.com/sohamchoudhury18/Houseofindya/blob/master/houseofindya/URL.csv)
[listing_data.csv](https://github.com/sohamchoudhury18/Houseofindya/blob/master/houseofindya/listing_data_2021-03-23T07-24-34.csv)
