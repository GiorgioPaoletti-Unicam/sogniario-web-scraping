import scrapy
from pymongo import MongoClient
from scrapy_splash import SplashRequest

script = """
-- Arguments:
-- * url - http://www.thedreamarchive.org;

-- main script
function main(splash, args)
    assert(splash:go(args.url))
    splash:set_viewport_full()

    local scroll_delay = 0.5
    local num_scrolls = 20
    local scroll_to = splash:jsfunc("window.scrollTo")

    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )

    for _ = 1, num_scrolls do
        scroll_to(0, get_body_height())
        splash:wait(scroll_delay)
    end

    return splash:html()
end
"""
url = 'http://www.thedreamarchive.org'


def parse_link(response):
    client = MongoClient()

    db = client['Dreams']
    collection = db['thedreamarchiveDreams']

    text_container = response.css('div.blog-item-content.e-content')

    collection.insert_one({
        "title": response.css('h2.entry-title.entry-title--large.p-name::text').get(),
        "text": '\n'.join(text_container.css('p::text').getall()),
        "date": response.css('time.dt-published.date-callout').attrib['datetime'],
    })


class ThedreamarchiveSpider(scrapy.Spider):
    name = 'thedreamarchiveSpider'

    def start_requests(self):
        yield SplashRequest(url, self.parse,
                            endpoint='execute',
                            cache_args=['lua_source'],
                            args={'lua_source': script},
                            )

    def parse(self, response):
        links_container = response.css('div#blogList')

        for link in links_container.css('a::attr(href)').getall():
            if link != '/?author=576d4e27e6f2e159370bbc1e':
                yield scrapy.Request(url + link, parse_link)
