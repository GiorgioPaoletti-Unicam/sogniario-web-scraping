import scrapy
from pymongo import MongoClient


def parse_link(response):
    client = MongoClient()
    db = client['Dreams']
    collection = db['internationalarchiveofdreamsDreams']

    row_container = response.css('div#comp-jh97l5gp')

    rows = row_container.css('p')

    dreams = []
    for r in rows:
        if r.css('span::text').get():
            for r_ in r.css('span::text').getall():
                dreams.append((r_.encode('ascii', 'ignore')).decode("utf-8"))
        else:
            dreams.append('')

    i = 0
    while True:

        if i + 5 > len(dreams):
            break

        if dreams[i + 1] != '':
            collection.insert_one({
                # "id": dreams[i],
                "title": dreams[i + 1],
                "text": dreams[i + 3],
                "date": None,
                "language": "en"
            })
            i += 5

        else:
            collection.insert_one({
                # "id": dreams[i],
                "title": None,
                "text": dreams[i + 2],
                "date": None,
                "language": "en"
            })
            i += 4


class InternationalarchiveofdreamsSpider(scrapy.Spider):
    name = 'internationalarchiveofdreamsSpider'
    start_urls = ['https://www.internationalarchiveofdreams.com/archive']

    def parse(self, response):

        links_container = response.css('div#comp-k7uqwkqe')

        for link in links_container.css('a'):
            yield scrapy.Request(link.attrib['href'], parse_link)
