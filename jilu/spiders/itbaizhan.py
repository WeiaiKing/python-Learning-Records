# -*- coding: utf-8 -*-
import scrapy


class ItbaizhanSpider(scrapy.Spider):
    name = 'itbaizhan'
    allowed_domains = ['itbaizhan.com']
    # start_urls = ['http://www.itbaizhan.cn/record?page={}'.format(num) for num in range(1,17)]
    # str = 'UM_distinctid=16924f16a671bf-0be344be91731a-b78173e-100200-16924f16a686c7; _ga=GA1.2.1727796524.1551102996; acw_tc=65c86a0915540887772513966e920e2906d2aee8c00d554b4b9c2c50ef780d; user=a%3A2%3A%7Bs%3A2%3A%22id%22%3Bi%3A8056%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2215677797686%22%3B%7D; token=DFB13079D757E78F3C7ADC8AA3A645F9; PHPSESSID=ieopcq2cqcmtbklittbfm3jjb3; CNZZDATA1273229192=28309065-1551098866-%7C1556433404'
    def start_requests(self):
        for i in range(1,17):
            url = 'http://www.itbaizhan.cn/record?page={}'.format(i)
            str = 'UM_distinctid=16924f16a671bf-0be344be91731a-b78173e-100200-16924f16a686c7; _ga=GA1.2.1727796524.1551102996; acw_tc=65c86a0915540887772513966e920e2906d2aee8c00d554b4b9c2c50ef780d; user=a%3A2%3A%7Bs%3A2%3A%22id%22%3Bi%3A8056%3Bs%3A5%3A%22phone%22%3Bs%3A11%3A%2215677797686%22%3B%7D; token=DFB13079D757E78F3C7ADC8AA3A645F9; PHPSESSID=ieopcq2cqcmtbklittbfm3jjb3; CNZZDATA1273229192=28309065-1551098866-%7C1556433404'
            cookies = {}
            for cookie in str.split(';'):
                key, value = cookie.split('=', 1)
                cookies[key] = value
            yield scrapy.Request(url, cookies=cookies, callback=self.parse)
    def parse(self, response):
        names = response.xpath('//a[@class = "record_course fl"]/text()').extract()
        times= response.xpath('//span[@class = "record_time fl"]/text()').extract()
        # print(name)
        # print(time)
        jilu = []
        for name,time in zip(names,times):
            jilu.append({
                'name': name,
                'tiem': time
            })
        return jilu

        # yield {
        #     'name': name,
        #     'tiem': time
        # }
        # books = []
        # for name, author in zip(names, authors):
        #     books.append({
        #         'name': name,
        #         'author': author
        #     })
        # return books
