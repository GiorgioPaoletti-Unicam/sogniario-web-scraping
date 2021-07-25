import scrapy
from pymongo import MongoClient


class InternationalarchiveofdreamsSpider(scrapy.Spider):
    name = 'internationalarchiveofdreamsSpider'
    start_urls = ['https://www.internationalarchiveofdreams.com/abstract']

    def parse(self, response):

        client = MongoClient()
        db = client['Dreams']
        collection = db['internationalarchiveofdreamsDreams']

        row_container = response.css('div._2bafp')

        rows = row_container.css('p')

        """
        dreams = rows.css('span::text').getall()
        
        i = 0
        while True:

            if i >= len(dreams):
                break
            
            if dreams[i + 1] == '\u200b' and dreams[i + 1] == '\xa0':
                collection.insert_one({
                    "id": dreams[i],
                    "title": dreams[i + 1],
                    # i + 2 --> \u200b o \xa0
                    "text": dreams[i + 3]
                    # i + 4 --> \u200b o \xa0
                })
                i = i + 5
            
            # if dreams[i + 1] == '\u200b' or dreams[i + 1] == '\xa0':
            # if dreams[i + 1] == " ":
            if (dreams[i + 1].encode('ascii', 'ignore')).decode("utf-8") is ' ':
                collection.insert_one({
                    "id": dreams[i],
                    # "title": '',
                    "text": dreams[i + 2]
                })
            i += 4
            
        """

        dreams = [(s.encode('ascii', 'ignore')).decode("utf-8") for s in rows.css('span::text').getall()]

        i = 0
        while True:

            if i + 5 > len(dreams):
                break

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


# <span class="wixGuard">​</span>                   \u200b      u"\u200B"
# <p class="font_8" style="font-size:17px">&nbsp;</p>   \xa0        u"\u00A0"

# NON FUNZIONA -> dreams[9] non contine uno "vuoto" ma contine diretamente l'ID di quello dopo
# AGGIUGERE L'ALGORITMO PER TUTTE LE PAGINE DEL SITO