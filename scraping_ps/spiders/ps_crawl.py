import scrapy
import json

class PsCrawlSpider(scrapy.Spider):
    name = "ps_crawl"
    allowed_domains = ["bit.ly"]
    start_urls = ["https://bit.ly/scrapingtry"]  # Ganti URL dengan URL yang benar

    def parse(self, response):
        games = response.css('a[data-telemetry-meta]')  # Ganti dari div ke a, karena data-telemetry-meta ada di elemen 'a'

        for game in games:
            meta_data = json.loads(game.attrib['data-telemetry-meta'])
            title = meta_data['name']
            price = meta_data['price']

            yield {
                'title': title,
                'price': price
            }
