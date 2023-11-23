from scrapy import Request, Spider


class QuotesToScrapeComSearchSpider(Spider):
    name = "quotes_toscrape_com_search"

    def start_requests(self):
        yield Request(
            "http://quotes.toscrape.com/search.aspx",
            meta={
                "zyte_api_automap": {
                    "browserHtml": True,
                    "actions": [
                        {
                            "action": "select",
                            "selector": {"type": "css", "value": "#author"},
                            "values": ["Albert Einstein"],
                        },
                        {
                            "action": "waitForSelector",
                            "selector": {
                                "type": "css",
                                "value": "[value=\"world\"]",
                                "state": "attached",
                            },
                        },
                        {
                            "action": "select",
                            "selector": {"type": "css", "value": "#tag"},
                            "values": ["world"],
                        },
                        {
                            "action": "click",
                            "selector": {"type": "css", "value": "[type='submit']"},
                        },
                        {
                            "action": "waitForSelector",
                            "selector": {"type": "css", "value": ".quote"},
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
                "text": quote.css(".content::text").get()[1:-1],
            }
