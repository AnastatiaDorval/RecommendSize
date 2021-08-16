import scrapy

class hmSpider(scrapy.Spider):
    name = 'hm'

    def start_requests(self):
        url = 'https://www2.hm.com/en_us/index.html'

