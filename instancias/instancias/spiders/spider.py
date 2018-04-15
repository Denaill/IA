import scrapy
from scrapy.spiders import CrawlSpider, Rule, Spider
from scrapy.linkextractors import LinkExtractor
from instancias.items import InstanciasItem
from scrapy.exceptions import CloseSpider

class InstanciaSpider(CrawlSpider):
    name = 'InstanciasTSP'
    allowed_domain = ['www.elib.zib.de']
    start_urls = ['http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/'] 

    rules = (
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//ul/li/i'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//ul/li/a[@href]')), 
                            callback = 'parse_item', follow= False)
    )

    def parse_item(self, response):
        in_item = InstanciasItem()
        count = 0
        #Con la informacion de in_item se importaran todos los campos
        in_item['name'] = response.xpath('//html/body/pre/text()').extract()
        yield in_item