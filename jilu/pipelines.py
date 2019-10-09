# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JiluPipeline(object):
    def open_spider(self, spider):
        self.filename = open('jilu1.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # info = item['title'] + '\n' + item['content'] + '\n'
        info = item['name'] + '\n'
        self.filename.write(info)
        self.filename.flush()
        return item

    def close_spider(self, spider):
        self.filename.close()

