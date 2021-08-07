import scrapy
from pymongo import MongoClient


def parse_link(response):
    client = MongoClient()
    db = client['Dreams']
    collection = db['cepeiDreams']

    for dream in response.css('p'):
        if dream.css('span::text').get() is None:
            continue

        collection.insert_one({
            "title": None,
            "text": dream.css('span::text').get(),
            "date": None,
            "language": "it"
        })


"""
Spider that deals with extracting data from the site www.cepei.it
"""


class CepeiSpider(scrapy.Spider):
    name = 'cepeiSpider'

    start_urls = ['https://www.cepei.it/i-sogni/']

    def parse(self, response):
        links = response.css('div.sogni')

        for url in links.css('a::text').getall():
            yield scrapy.Request('https://www.cepei.it/' + url, parse_link)

# scrapy crawl nameSpider
