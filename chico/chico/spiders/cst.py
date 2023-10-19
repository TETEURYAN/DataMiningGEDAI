import scrapy


class CstSpider(scrapy.Spider):
    name = "cst"
    allowed_domains = ["chicosabetudo.com"]
    start_urls = ["https://chicosabetudo.com"]

    def parse(self, response):
        pass
