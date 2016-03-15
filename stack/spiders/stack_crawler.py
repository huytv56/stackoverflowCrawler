import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['http://stackoverflow.com/questions?pagesize=50&sort=newest']

    rules = (
        Rule(LinkExtractor(allow=r'questions/[0-9]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = StackItem()
        item['url'] = response.xpath(
            '//div[@id="question-header"]/h1/a/@href').extract()[0]
        item['title'] = response.xpath(
            '//div[@id="question-header"]/h1/a/text()').extract()[0]


        yield item