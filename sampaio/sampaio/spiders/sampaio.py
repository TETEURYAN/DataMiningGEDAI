import scrapy
import requests
from bs4 import BeautifulSoup


class CstSpider(scrapy.Spider):
    name = "sampaio"
    allowed_domains = ["radiosampaio.com.br"]
    start_urls = ["https://radiosampaio.com.br/?s=palmeira+dos+indios+policia"]

    def parse(self, response):

        links = response.css('.oxy-post-image').getall()

        for aux in links:
            soup = BeautifulSoup(aux, 'html.parser')
            ref = soup.a.get('href')

            url = requests.get(ref)

            html = url.text
            linked = BeautifulSoup(html, 'html.parser')
            titulo = linked.find("span", class_ = "ct-span").text
            author = linked.find("span", {"id" : "span-17-109213"}).text
            data = linked.find("span", {"id" : "span-20-109213"}).text

            yield {
               'title': titulo,
               'author' : author,
               'date' : data,
               'link' : ref,
            }
        nextpage = response.xpath('//*[@id="_posts_grid-7-109385"]/div[2]/a[4]').get()
        
        auxiliar = BeautifulSoup(nextpage, 'html.parser')
        page = auxiliar.a.get('href')
        if page is not None:
            yield response.follow(page,callback = self.parse)   
        




        
        
