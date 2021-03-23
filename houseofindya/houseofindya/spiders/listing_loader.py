import scrapy
import pandas as pd
import re

class Listingscraper(scrapy.Spider):
    name = "listing_scraper"

    df = pd.read_csv("URL.csv")
    
    allowed_domains = ['houseofindya.com']

    custom_settings={ 'FEED_URI': "listing_data.csv",
                       'FEED_FORMAT': 'csv'}

    start_urls = list(df["URL"])

    def parse(self,response):
        data = response.css("div.prodRight")
        
        ##Title 
        title = data.css("h1::text").get()

        ##price
        price = data.css("span::text").getall()[2]

        ##Description
        product_description = data.css("#tab-1").css("p::text").get()

        ##Details
        details = data.css("#tab-2").css("p::text").getall()[:-7]
        c_name = []
        c_val = []
        for d in details:
            if re.search("[-:]",d) != None:
                s = re.split("[-:]",d)
                c_name.append(s[0])
                c_val.append(s[1])

        detail_dict = dict(zip(c_name,c_val))
        
        ##Images
        img_data = response.css("#productsections").css("img").xpath("@data-original").getall()
        img_index = ["img1","img2","img3","img4","img5"]
        img_dict = dict(zip(img_index,img_data))

        dict_1 = {"URL":response.url,"Title":title,"Price":price,"Description":product_description,**detail_dict,**img_dict}
        yield dict_1

    

        

        

        
        
