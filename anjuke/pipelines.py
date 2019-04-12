# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb.cursors


class AnjukePipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    # 自己写的导进mysql数据库的pipeline
    def __init__(self):
        # 这里自己填连接mysql的属性
        self.conn = MySQLdb.connect('host', 'user', 'password', 'dbname', charset="utf-8", use_unicode=True)

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into anju(title, size, total_price, locate, meter_price,crawl_time)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['size'], item['total_price'], item['locate'],
                                         item['meter_price'], item['crawl_time']
                                         ))
        self.conn.commit()
