import scrapy
import pandas as pd

class Test1Spider(scrapy.Spider):
    name = "urlspider"

    allowed_domains = ['houseofindya.com']

    start_urls = [
            "https://www.houseofindya.com/zyra/necklace-sets/cat"
        ]

    
    def parse(self, response):
        
        data = response.css("#JsonProductList")
        data_list = data.xpath("//li[@data-cat='Indya Clothing']")
        self.log(len(data_list))
        url_list = []
        for l in data_list:
            url_list.append(l.xpath("@data-url").get())
        
        data_list_df = pd.DataFrame(url_list,columns=["URL"])
        data_list_df.to_csv("URL.csv",index=False)
        self.log(data_list_df)
        


        

        
