from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "get_products"

    def start_requests(self):
        urls = [
            'https://www.croma.com/hitachi-kiyora-5100x-1-5-ton-4-star-hot-cold-inverter-split-ac-copper-condenser-superfine-mesh-filter-rsrg517hexa-/p/259677',
            'https://www.croma.com/carrier-indus-cxi-4-in-1-convertible-1-5-ton-3-star-hybridjet-inverter-split-smart-ac-with-dust-filter-2022-model-copper-condenser-cai18in3r31f1-/p/250035'

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        key_features = response.xpath('//div[@class = "key-features-box"]/div/ul/li/text()').extract()
        filename = 'key_feature.json'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')
