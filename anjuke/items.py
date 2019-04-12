# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from anjuke.tools.item_tools import remove_n,get_nums
import re

# class AnjukeItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class AnjukeItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()


class AnjukeItem(scrapy.Item):
    title = scrapy.Field(
        input_processor=MapCompose(remove_n),
    )
    size = scrapy.Field()
    # build_year = scrapy.Field()
    locate = scrapy.Field()
    total_price = scrapy.Field()
    meter_price = scrapy.Field(
        input_processor=MapCompose(get_nums),
    )
    crawl_time = scrapy.Field()
