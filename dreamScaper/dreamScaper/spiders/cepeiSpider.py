import scrapy
from pymongo import MongoClient


class CepeiSpider(scrapy.Spider):
    name = 'cepeiSpider'
    start_urls = ['https://www.cepei.it/morte/']

    def parse(self, response):

        client = MongoClient()
        db = client['Dreams']
        collection = db['cepeiDreams']

        for dream in response.css('p'):
            if dream.css('span::text').get() is None:
                continue

            collection.insert_one({"text": dream.css('span::text').get()})

            '''
            yield {
                'text': dream.css('span::text').get()
            }
            # scrapy crawl cepeiSpider -o dreams.json
            '''

# scrapy crawl nameSpider