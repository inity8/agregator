import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)

            def parse(self, response):
                for car_div in response.css('.ListingCars-module__listingItem'):
                    link = car_div.css('a.ListingItemTitle-module__link')
                    title = link.css('::text').get()
                    href = link.css('::attr(href)').get()

                    raw_price = car_div.css('.ListingItemPrice-module__content::text').get()

                    price = raw_price and clean_price(raw_price) or None

                    img_urls = car_div.css('.Brazzers__image::attr(data-src)').getall()
                    yield {
                        'title': title,
                        'href': href,
                        'price_eur': price,
                        'imgs': [response.urljoin(img) for img in img_urls],
                    }