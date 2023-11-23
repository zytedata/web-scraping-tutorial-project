import json
from scrapy import Spider


class QuotesToScrapeComScrollAPISpider(Spider):
    name = "quotes_toscrape_com_scroll_api"
    start_urls = [
        f"http://quotes.toscrape.com/api/quotes?page={n}" for n in range(1, 11)
    ]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data["quotes"]:
            yield {
                "author": quote["author"]["name"],
                "tags": quote["tags"],
                "text": quote["text"],
            }
