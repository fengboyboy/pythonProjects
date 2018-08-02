
# -- scrapy框架爬虫

import scrapy

# -- 创建继承spider的爬虫类
class cgmscrapy(scrapy.Spider):
    name = "cgm"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]

    # unseen = set()
    # seen = set()      # we don't need these two as scrapy will deal with them automatically

    def parse(self, response):
        yield {  # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')  # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)  # it will filter duplication automatically


