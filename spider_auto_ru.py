import scrapy

# def clean_price(text):
#     digits = [symbol for symbol in text if symbol.isdigit()]
#     cleaned_text = ''.join(digits)
#     if not cleaned_text:
#         return None
#     return int(cleaned_text)


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://auto.ru/balashiha/cars/tesla/all/?currency=EUR']

    def parse(self, response):
        # for car_div in response.css('.ListingCars-module__listingItem'):
        # for car_div in response.css('.ListingItemTitle-module__clicker'):
        for car_div in response.css('.ListingItem-module__columnCellSummary'):
            link = car_div.css('a.ListingItemTitle-module__link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()

            # raw_price = car_div.css('.ListingItemPrice-module__content::text').get()

            price = 1
                # raw_price and clean_price(raw_price) or None

            img_urls = car_div.css('.Brazzers__image::attr(data-src)').getall()
            yield {
                'title': title,
                'href': href,
                'price_eur': price,
                'imgs': [response.urljoin(img) for img in img_urls],
            }