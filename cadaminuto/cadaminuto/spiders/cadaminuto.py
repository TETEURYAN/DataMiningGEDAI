import scrapy


class CadaminutoSpider(scrapy.Spider):
    name = "cadaminuto"
    allowed_domains = ["cadaminuto.com"]
    start_urls = ["https://cadaminuto.com"]

    def parse(self, response):
        pass
