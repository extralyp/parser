import scrapy


class DotabuffSpider(scrapy.Spider):
    name = 'dotabuff'
    allowed_domain = ['https://ru.dotabuff.com']
    start_urls = ['https://ru.dotabuff.com/players/28131058/matches?enhance=overview&page=1']

    def parse(self,response):
        for quote in response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr[1]'):
            for a in range(1, len(response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr'))+1):
                yield {
                    'date': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[4]/div/time/@datetime').get(),
                    'hero': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[2]/a/text()').get(),
                    'rang': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[2]/div/text()').get(),
                    'mode': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[5]/div/text()').get(),
                    'result': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[4]/a/text()').get(),
                    'time': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[6]/text()').get(),
                    'kills': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[7]/span/span[1]/text()').get(),
                    'deaths': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[7]/span/span[2]/text()').get(),
                    'assists': quote.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/table/tbody/tr['+str(a)+']/td[7]/span/span[3]/text()').get(),
                    }

        next_page = response.xpath('/html/body/div[1]/div[8]/div[2]/div[3]/section/section/article/nav/span[7]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)