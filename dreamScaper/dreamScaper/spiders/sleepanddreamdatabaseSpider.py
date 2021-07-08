import scrapy
from pymongo import MongoClient
from scrapy_splash import SplashRequest
import json


class SleepanddreamdatabaseSpider(scrapy.Spider):
    name = 'sleepanddreamdatabaseSpider'

    '''
        def start_requests(self):
        url = 'https://sleepanddreamdatabase.org/search_results/falling_dreams'

        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        client = MongoClient()
        db = client['Dreams']
        collection = db['sleepanddreamdatabaseDreams']

        for dream in response.css('a.sc-pciXn.kKVZfa').getall():
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

    '''

    start_urls = ['https://sleepanddreamdatabase.org/search_results/falling_dreams']

    headers = {
        "Authority": "api.sleepanddreamdatabase.org",
        "Method": "POST",
        "Path": "/graphql",
        "Scheme": "https",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Content-Length": 990,
        "Content-Type": "application/json",
        "Dnt": 1,
        "Origin": "https://sleepanddreamdatabase.org",
        "Referer": "https://sleepanddreamdatabase.org/",
        "Sec-Ch-Ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"91\", \"Chromium\";v=\"91\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }

    def parse(self, response):
        url = 'https://api.sleepanddreamdatabase.org/graphql'

        yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)

    def parse_api(self, response):
        client = MongoClient()
        db = client['Dreams']
        collection = db['sleepanddreamdatabaseDreams']

        raw_data = response.body
        data = json.loads(raw_data)

        for dream in data['aWordSearch']['answers']:
            collection.insert_one(
                {
                    "text": dream['_source']['answer_text'],
                    "dreamerId": dream['_source']['response_set']['respondent']['user_name'],
                    "date": dream['_source']['response_set']['created_at']
                }
            )



#https://www.youtube.com/watch?v=lKIXRAtromY&t=2905s