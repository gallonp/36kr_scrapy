import scrapy
from tutorial.items import KrItem
class KrSpider(scrapy.Spider):
    name = "36kr_spider"
    allowed_domains = ["36kr.com"]
    start_urls = [
        "http://www.36kr.com"
    ]

    def parse(self, response):
        articles =  response.xpath('//div[@class="articles"]/article')
        filename = 'test3.txt'
        with open(filename, 'wb') as f:
            for article in articles:
                it = KrItem()
                title = article.xpath('./div[@class="right-col"]/h1/a/text()').extract()
                it['title'] = title#unicode(title).encode("utf8")
                description =  article.xpath('./div[@class="right-col"]/p/text()').extract()
                image_urls =  article.xpath('.//div[@class="image feature-img thumb-180"]/a/img/@data-src').extract()
                it['description'] = description#unicode(description).encode("utf8")
                it['image_urls'] = image_urls
                yield(it)
        f.close()