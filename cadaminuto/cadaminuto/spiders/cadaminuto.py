import scrapy


class CadaminutoSpider(scrapy.Spider):
    name = "cadaminuto"
    allowed_domains = ["cadaminuto.com"]
    start_urls = ["https://www.cadaminuto.com.br/busca?q=arapiraca+seguran%C3%A7a"]

    def parse(self, response):
        
