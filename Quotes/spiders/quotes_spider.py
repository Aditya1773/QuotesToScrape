import scrapy
from ..items import QuotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls=[
        'https://quotes.toscrape.com/'
    ]
    def parse(self, response):
        items=QuotesItem()

        all_div_quotes=response.css('div.quote')

        for quotes in all_div_quotes:

            title=quotes.css('span.text::text').extract()
            author=quotes.css('small.author::text').extract()
            tag=quotes.css('a.tag::text').extract()
            items['title']=title
            items['author']=author
            items['tag']=tag
            yield items







