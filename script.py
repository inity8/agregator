import scrapy

class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://auto.ru/cars/tesla/all/']

    def parse(self, response):
        for car_div in response.css('a.ListingCars-module__container ListingCars-module__list'):
            link = car_div.css('a.Link ListingItemTitle-module__link').get()
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()


            yield {
                'title': title,
                'href': href,
            }
        #
        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)
