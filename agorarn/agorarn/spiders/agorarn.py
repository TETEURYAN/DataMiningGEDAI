import scrapy
import requests
from bs4 import BeautifulSoup


class AgorarnSpider(scrapy.Spider):
    name = "agorarn"
    allowed_domains = ["natalemfoco.com.br"]
    start_urls = ["https://natalemfoco.com.br/policia/"]

    def parse(self, response):
        links = response.css('.desc-not-lista').getall()

        for tag in links:
        # Parseia a tag com BeautifulSoup
            soup = BeautifulSoup(tag, 'html.parser')

            # Encontra a tag <span> que contém o título da matéria
            titulo_tag = soup.find("div", class_="titulo-sub-lista").span.text

            # # Extrai o texto do título
            # titulo = titulo_tag.text.strip()

            yield {
               'title': titulo_tag,
            }

        nextpage = response.css('.nextpostslink').get()

        auxiliar = BeautifulSoup(nextpage, 'html.parser')
        page = auxiliar.a.get('href')    

        if page is not None:
            yield response.follow(page,callback = self.parse) 
        pass
