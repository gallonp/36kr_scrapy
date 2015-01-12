from scrapy.exceptions import DropItem

class krPipeline(object):


    def process_item(self, item, spider):
        if item['title'] && item['description']:
            print 'rageagweg'
            return item
        else:
            raise DropItem("Missing title or description in %s" % item)