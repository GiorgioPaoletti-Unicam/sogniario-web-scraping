import scrapy
from pymongo import MongoClient


def parse_link(response):
    client = MongoClient()
    db = client['Dreams']
    collection = db['internationalarchiveofdreamsDreams']

    row_container = response.css('div._2bafp')

    rows = row_container.css('p')

    # dreams = rows.css('span::text').getall()
    dreams = [(s.encode('ascii', 'ignore')).decode("utf-8") for s in rows.css('span::text').getall()]

    i = 0
    while True:

        if i + 5 > len(dreams):
            break

        # if dreams[i + 1] == '\u200b' and dreams[i + 1] == '\xa0':
        if dreams[i + 1] != '':
            collection.insert_one({
                "id": dreams[i],
                "title": dreams[i + 1],
                "text": dreams[i + 3]
            })
            i += 5

        else:
            collection.insert_one({
                "id": dreams[i],
                "text": dreams[i + 2]
            })
            i += 4


class InternationalarchiveofdreamsSpider(scrapy.Spider):
    name = 'internationalarchiveofdreamsSpider'
    start_urls = ['https://www.internationalarchiveofdreams.com/archive']

    def parse(self, response):
        links_container = response.css('div._2bafp')

        for link in links_container.css('a'):
            yield scrapy.Request(link.attrib['href'], parse_link)

# <span class="wixGuard">​</span>                   \u200b      u"\u200B"
# <p class="font_8" style="font-size:17px">&nbsp;</p>   \xa0        u"\u00A0"

# NON FUNZIONA -> dreams[9] non contine uno "vuoto" ma contine diretamente l'ID di quello dopo
