from scrapy import Request, Spider


class QuotesToScrapeComScrollBrowserSpider(Spider):
    name = "quotes_toscrape_com_scroll_browser"

    def start_requests(self):
        yield Request(
            "http://quotes.toscrape.com/scroll",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "actions": [
                        {
                            "action": "scrollBottom",
                        },
                    ],
                },
            },
        )

    def parse(self, response):
        for quote in response.css(".quote"):
            yield {
                "author": quote.css(".author::text").get(),
                "tags": quote.css(".tag::text").getall(),
                "text": quote.css(".text::text").get()[1:-1],
            }
