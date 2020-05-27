import scrapy

# <div> 3 & nbsp;150 & nbsp;000 & nbsp;₽ </div>


def clean_price(text):
    digits = [symbol for symbol in text if symbol.isdigit()]
    cleaned_text = ''.join(text)
    if not cleaned_text:
        return None
    return int(cleaned_text)

# print(clean_price("4\u00a0525\u00a0120\u00a0\u20bd"))
# exit()


class Spider(scrapy.Spider):
    name = 'spider'
    start_urls = ['https://auto.ru/cars/tesla/all/?currency=EUR']

    def parse(self, response):
        for car_div in response.css('.ListingCars-module__listingItem'):
            link = car_div.css('a.ListingItemTitle-module__link')
            title = link.css('::text').get()
            href = link.css('::attr(href)').get()
            raw_price = car_div.css('.ListingItemPrice-module__content::text').get()
            price = raw_price and clean_price(raw_price) or None

            yield {
                'title': title,
                'href': href,
                'price': price,
            }


