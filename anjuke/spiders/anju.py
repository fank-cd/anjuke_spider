# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from anjuke.items import AnjukeItemLoader, AnjukeItem
from urllib import parse
from datetime import datetime


class AnjuSpider(scrapy.Spider):
    name = 'anju'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://chengdu.anjuke.com/sale/']

    def parse(self, response):
        nodes = response.xpath(".//div[@class='house-title']/a/@href").extract()
        for node_url in nodes:
            yield Request(url=parse.urljoin(response.url, node_url), callback=self.parse_item)

        next_url = response.xpath("//a[@class='aNxt']/@href").extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_item(self, response):

        item_loader = AnjukeItemLoader(item=AnjukeItem(), response=response)

        item_loader.add_xpath("title", "//h3[@class='long-title']/text()")
        item_loader.add_xpath("size", "//span[@class='info-tag'][2]/em/text()")
        item_loader.add_xpath("total_price", "//span[@class='light info-tag']/em/text()")
        item_loader.add_xpath("locate", "//div[@class='houseInfo-content']/p/a[1]/text()")
        meter_price = response.xpath("//div[@class='houseInfo-content']")[2].xpath("text()").extract_first("")
        item_loader.add_value("meter_price", meter_price)
        crawl_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        item_loader.add_value("crawl_time", crawl_time)
        anjuke_item = item_loader.load_item()

        yield anjuke_item

