import scrapy
from pymongo import MongoClient
from scrapy_splash import SplashRequest


class SleepanddreamdatabaseSpider(scrapy.Spider):
    name = 'sleepanddreamdatabaseSpider'

    def start_requests(self):
        url = 'https://sleepanddreamdatabase.org/search_results/falling_dreams'

        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        client = MongoClient()
        db = client['Dreams']
        collection = db['sleepanddreamdatabaseDreams']

        for dream in response.css('div.sc-pJVnX.jOExFg'):
            dream_text = dream.css('div.sc-pjGMk.jrwOpx')

            dream_info = dream.css('div.sc-qZtVr.dLIPjF')

            collection.insert_one(
                {
                    "text":
                        dream_text.css('span::text').get(0) +
                        dream_text.css('mark::text').get() +
                        dream_text.css('span::text').get(1),
                    "dreamerId": dream_info.css('div.sc-pzLqt.jakOsZ').get(0).css('div::text').get(1),
                    "date": dream_info.css('div.sc-pzLqt.jakOsZ').get(1).css('div::text').get(1)
                }
            )
