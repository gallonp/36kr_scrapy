# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item




class krPipeline(object):


    def process_item(self, item, spider):
        if not item['title']==[] and not item['description']==[]:
            print 'rageagweg'
            return item
        else:
            raise DropItem("Missing title or description in %s" % item)