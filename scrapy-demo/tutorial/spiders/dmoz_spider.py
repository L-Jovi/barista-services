# coding: utf-8

import scrapy
from tutorial.items import DmozItem
# from redis import Redis


class DmozSpider(scrapy.Spider):

    name = "dmoz"
    allowed_domains = ["dmoz.org"]

    # basic start url
    # start_urls = [
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    #     "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    # ]

    # basic practice
    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    # improving practice
    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item["link"] = sel.xpath('a/@href').extract()
    #         item["desc"] = sel.xpath('text()').extract()
    #         yield

    # some pagination parse method
    # but we don't use it now
    def parse_articles_follow_next_page(self, response):
        for article in response.xpath("//article"):
            item = DmozItem()

            # ... extract article data here

            yield item

        next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse_articles_follow_next_page)


    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/",
    ]

    # init redis
    # cli = Redis('127.0.0.1', 6379, db=1)

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())

            # self.cli.lpush('dmoz_url', url)
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
