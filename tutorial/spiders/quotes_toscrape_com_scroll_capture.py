import json
from base64 import b64decode

from scrapy import Request, Spider


class QuotesToScrapeComScrollCaptureSpider(Spider):
    name = "quotes_toscrape_com_scroll_capture"

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
                    "networkCapture": [
                        {
                            "filterType": "url",
                            "httpResponseBody": True,
                            "value": "/api/",
                            "matchType": "contains",
                        },
                    ],
                },
            },
        )

    def parse(self, response):
        for capture in response.raw_api_response["networkCapture"]:
            text = b64decode(capture["httpResponseBody"]).decode()
            data = json.loads(text)
            for quote in data["quotes"]:
                yield {
                    "author": quote["author"]["name"],
                    "tags": quote["tags"],
                    "text": quote["text"],
                }
