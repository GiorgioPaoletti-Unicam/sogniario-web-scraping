import scrapy
from pymongo import MongoClient


class SleepanddreamdatabaseSpider(scrapy.Spider):
    name = 'sleepanddreamdatabaseSpider'
    start_urls = ['https://sleepanddreamdatabase.org/search_results/falling_dreams']

    def parse(self, response):

        client = MongoClient()
        db = client['Dreams']
        collection = db['sleepanddreamdatabaseDreams']

        '''
        for dream in response.css('p'):
            if dream.css('span::text').get() is None:
                continue

            collection.insert_one({"text": dream.css('span::text').get()})
        '''
